import datetime
import pymysql
import asyncio as aio
from typing import List
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio

from repositorios.clienteRepositorio import UsuarioRepository
from repositorios.escritorioRepositorio import EscritorioRepositorio
from repositorios.ferramentasRepositorio import ApiFerramentas

from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados
from modelos.tetosPrevORM import TetosPrev
from modelos.convMonORM import ConvMon
from modelos.indicadoresORM import Indicadores
from modelos.expSobrevidaORM import ExpSobrevida
from modelos.carenciasLei91 import CarenciaLei91
from modelos.indiceAtuMonetariaORM import IndiceAtuMonetaria
from modelos.configGeraisORM import ConfigGerais
from modelos.salarioMinimoORM import SalarioMinimo
from modelos.ipcaMensalORM import IpcaMensal

from Design.pyUi.loginPage import Ui_mwLogin

from heart.dashboard.dashboardController import DashboardController
from heart.newDashboard.newDashboard import NewDashboard

from util.dateHelper import strToDatetime
from util.enums.newPrevEnums import *
from util.enums.ferramentasEInfoEnums import FerramentasEInfo

import os
import json

from util.ferramentas.tools import divideListaEmPartes
from util.helpers import datetimeToSql
from util.popUps import popUpOkAlerta

from repositorios.informacoesRepositorio import ApiInformacoes


class LoginController(QMainWindow, Ui_mwLogin):

    def __init__(self, db=None):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.db = db
        self.usuarioRepositorio = UsuarioRepository()
        self.escritorio: Escritorios = Escritorios()
        self.advogado: Advogados = Advogados()
        self.escritorioRepositorio = EscritorioRepositorio()
        self.tentativasSenha = 3
        self.edittingFinished = True
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.pbarLoading.hide()
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.escondeLoading)

        self.configGerais = ConfigGerais()

        self.daoEscritorio = Escritorios()
        self.daoAdvogado = Advogados(self.db)

        self.dashboard: DashboardController = None

        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
        # self.pbPrimeiroAcesso.clicked.connect(self.iniciarPrimeiroAcesso)
        self.pbCancelar.clicked.connect(self.cancelaCadastro)
        self.pbCadastrar.clicked.connect(self.avaliaConfirmacaoCadastro)
        self.pbFechar.clicked.connect(self.close)
        self.pbEntrar.clicked.connect(self.entrar)

        self.iniciaCampos()
        self.carregaCacheLogin()

        if self.advogado:
            self.iniciarAutomaticamente()

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def iniciarPrimeiroAcesso(self):
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.cadastro.value)
        self.trocaPagina(self.advogado)
        self.leSenhaProvisoria.setText(self.advogado.senha)
        self.buscaEscritorio(self.advogado.escritorioId.escritorioId)

    def iniciarAutomaticamente(self):
        pass

    def carregaCacheLogin(self):
        self.advogado = self.cacheLogin.carregarCache()
        if self.advogado.numeroOAB is not None:

            # Confere informações do escritório
            # self.escritorio = self.escritorioRepositorio.buscaEscritorio(self.advogado.escritorioId)
            try:
                self.escritorio = Escritorios.select().where(Escritorios.escritorioId == self.advogado.escritorioId).get()
            except Escritorios.DoesNotExist:
                self.escritorio = Escritorios()
                self.escritorio.escritorioId = None

            if isinstance(self.escritorio, ErroConexao):
                self.apresentandoErros(self.escritorio)
                return False
            elif self.escritorio:
                self.cacheEscritorio.salvarCache(self.escritorio)
            else:
                self.cacheLogin.limpaCache()
                self.cacheEscritorio.limpaCache()
                popUpOkAlerta("Erro ao buscar informações do escritório.\nTente novamente mais tarde")
                return False

            self.lbNomeDoEscritorio.setText(self.escritorio.nomeFantasia)
            self.leLogin.setText(self.advogado.numeroOAB)
            self.leSenha.setText(self.advogado.senha)
            self.cbSalvarSenha.setChecked(True)
        else:
            self.advogado = Advogados()
            self.cacheLogin.limpaCache()
            self.cacheEscritorio.limpaCache()
            self.leLogin.setFocus()

    def trocaPagina(self, advogadoModel: Advogados):
        if advogadoModel is None:
            print('trocaPagina')
            return False
        advogado: Advogados = advogadoModel
        self.advogado = advogado
        senhaProvisoria = self.usuarioRepositorio.buscaSenhaProvisoria(advogado.advogadoId)

        if "erro" in senhaProvisoria.keys():
            popUpOkAlerta(f"Advogado(a) não encontrado(a). Favor acessar o cadastro do escritório ou o contratante do sistema.")
            return False
        else:
            self.advogado.senha = senhaProvisoria['senha']

        self.lePrimCadLogin.setText(advogado.login)
        self.leNome.setText(advogado.nomeUsuario)
        self.leSobrenome.setText(advogado.sobrenomeUsuario.strip())
        self.leEmail.setText(advogado.email[0])
        self.leNacionalidade.setText(advogado.nacionalidade)
        self.leEstadoCivil.setText(advogado.estadoCivil)
        self.lbNumeroDaOAB.setText(advogado.numeroOAB)
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.cadastro.value)

    def cancelaCadastro(self):
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
        self.limpa()
        self.limpaListaAdv()

    def buscaEscritorio(self, escritorioId: int):
        if escritorioId is None:
            popUpOkAlerta(
                f'Não foi possível encontrar o escritório na qual o advogado {self.advogado.nomeUsuario} está cadastrado. Entre em contato com o suporte.',
                erro=f'buscaEscritorio<LoginController> escritorioId: {escritorioId}'
            )
            return False

        if escritorioId > 0:
            escritorio: Escritorios = self.usuarioRepositorio.buscaEscritorioPrimeiroAcesso(escritorioId)
            self.escritorio = escritorio
            if escritorio and escritorio.escritorioId == escritorioId:
                self.lbNomeDoEscritorio.setText(escritorio.nomeFantasia)
            else:
                self.lbNomeDoEscritorio.setText('')

    def avaliaConfirmacaoCadastro(self):

        if self.leSenhaProvisoria.text() != self.advogado.senha:
            self.tentativasSenha -= 1
            popUpOkAlerta(f"Senha provisória diferente da cadastrada. Tente novamente. \nTentativas faltantes: {self.tentativasSenha}")
            if self.tentativasSenha == 0:
                self.close()
        elif self.lePrimCadSenha.text() != self.leConfirmarSenha.text():
            popUpOkAlerta(f"Senhas não coincidem. Tente novamente.")
        else:
            senhaConfirmada = self.usuarioRepositorio.atualizaSenha(self.advogado.advogadoId, self.leConfirmarSenha.text())
            self.loading(10)
            if 'statusCode' not in senhaConfirmada.keys():
                self.loading(10)
                self.advogado.senha = senhaConfirmada['senha']
                self.loading(20)
                self.leLogin.setText(self.advogado.numeroOAB)
                self.loading(10)
                self.leSenha.setText(self.advogado.senha)
                self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
                self.loading(10)
                self.cacheLogin.salvarCache(self.advogado)

                try:
                    self.advogado: Advogados = Advogados.get_by_id(self.advogado.advogadoId)
                    self.advogado.confirmado = True
                    self.advogado.dataUltAlt = datetime.datetime.now()
                    self.advogado.save()

                except Advogados.DoesNotExist:
                    Advogados.create(**self.advogado.toDict())

                self.loading(20)
                self.cacheEscritorio.salvarCache(self.escritorio)
                self.loading(10)
                # self.daoEscritorio.insereEscritorio(self.escritorio)
                self.escritorio.dataUltAlt = datetime.datetime.now()
                self.escritorio.save()
                self.loading(10)
            else:
                self.loading(100)
                popUpOkAlerta(f"Não foi possível confirmar o cadastro. Tente novamente.")

    def entrar(self):
        # TODO: Criar uma verificação se o usuário salvo em cache tem o mesmo login e senha digitado na tela de login

        loop = aio.get_event_loop()

        self.loading(20)
        if self.infoNaoNulo:
            if ApiFerramentas().conexaoOnline():
                self.loading(10)
                self.verificaRotinaAtualizacao()
                self.loading(20)
            else:
                popUpOkAlerta('Sem conexão com o servidor.')
                return False

            # Autentica advogado
            self.advogado = self.procuraAdvogado()

            if self.advogado:
                if not self.advogado.confirmado:
                    self.iniciarPrimeiroAcesso()
                    return True

                # Autentica escritório
                self.escritorio = self.procuraEscritorio(self.advogado.escritorioId)
                if self.escritorio:
                    escritorioCadastrado = Escritorios.get_by_id(self.escritorio.escritorioId)
                    advogadoCadastrado = Advogados.get_by_id(self.advogado.advogadoId)

                    if not escritorioCadastrado:
                        self.daoEscritorio.insereEscritorio(self.escritorio)
                    if not advogadoCadastrado:
                        self.daoAdvogado.insereAdvogado(self.advogado)

                    # Decide se salva informações no "temporários", dependendo do checkBox
                    if self.cbSalvarSenha.isChecked():
                        self.cacheLogin.salvarCache(self.advogado)
                        self.cacheEscritorio.salvarCache(self.escritorio)
                    else:
                        self.cacheLogin.salvarCacheTemporario(self.advogado)
                        self.cacheEscritorio.salvarCacheTemporario(self.escritorio)

                    # Busca e define configurações
                    try:
                        ConfigGerais.get(ConfigGerais.advogadoId == self.advogado.advogadoId)
                    except ConfigGerais.DoesNotExist:
                        ConfigGerais(advogadoId=self.advogado).save()

                    # Inicia programa
                    self.iniciaDashboard()

                else:
                    popUpOkAlerta("Houve um problema ao encontrar o escritório no banco de dados. Entre em contato com o suporte.")
                    self.cacheLogin.limpaCache()
                    self.cacheEscritorio.limpaCache()
                    # TODO: Lógica para clicar no botão "Ok" e fechar o programa
            else:
                self.tentativasSenha -= 1
                popUpOkAlerta("Usuário ou senha inválidos. Tente novamente")
                self.cacheLogin.limpaCache()
                self.cacheEscritorio.limpaCache()
                # TODO: Lógica para clicar no botão "Ok" e fechar o programa
                if self.tentativasSenha == 0:
                    popUpOkAlerta("A quantidade de tentativas excedeu o limite e o programa será fechado.")

        else:
            popUpOkAlerta("Campo login e senha precisam ser preenchidos")
            self.limpa()

        self.edittingFinished = True

    def iniciaDashboard(self):
        self.dashboard = NewDashboard()
        # self.dashboard = DashboardController()
        self.dashboard.iniciaDash()
        self.dashboard.showMaximized()
        self.close()

    def infoNaoNulo(self):
        login: bool = self.leLogin.text() != ''
        senha: bool = self.leSenha.text() != ''

        return login and senha

    def procuraAdvogado(self) -> Advogados:
        senha = self.leSenha.text()

        if self.leLogin.text().isdecimal():
            numeroOAB = self.leLogin.text()
            return self.usuarioRepositorio.loginAuth(senha, numeroOAB=numeroOAB)
        else:
            email = self.leLogin.text()
            return self.usuarioRepositorio.loginAuth(senha, email=email)

    def procuraEscritorio(self, escritorioId: int) -> Escritorios:
        escritorio: Escritorios = self.escritorioRepositorio.buscaEscritorio(escritorioId)
        return escritorio

    def verificaRotinaAtualizacao(self):

        pathFile = os.path.join(os.getcwd(), '.sync', '.syncFile')
        syncJson = {
            'syncConvMon': datetimeToSql(datetime.datetime.now()),
            'syncTetosPrev': datetimeToSql(datetime.datetime.now()),
            'syncIndicadores': datetimeToSql(datetime.datetime.now()),
            'syncExpSobrevida': datetimeToSql(datetime.datetime.now()),
            'syncCarenciasLei91': datetimeToSql(datetime.datetime.now()),
            'syncAtuMonetaria': datetimeToSql(datetime.datetime.now()),
            'syncSalarioMinimo': datetimeToSql(datetime.datetime.now()),
            'syncIpca': datetimeToSql(datetime.datetime.now()),
        }
        loop = aio.get_event_loop()

        if os.path.isfile(pathFile):
            with open(pathFile, encoding='utf-8', mode='r') as syncFile:
                if len(syncFile.readlines()) == 0:
                    os.remove(pathFile)
                    self.verificaRotinaAtualizacao()
                    return True
                else:
                    infoToUpdate = {}
                    syncFile.seek(0)
                    syncDict = json.load(syncFile)

                    dateSyncConvMon = strToDatetime(syncDict['syncConvMon'])
                    dateSyncTetosPrev = strToDatetime(syncDict['syncTetosPrev'])
                    dateSyncIndicadores = strToDatetime(syncDict['syncIndicadores'])
                    dateSyncExpSobrevida = strToDatetime(syncDict['syncExpSobrevida'])
                    dateSyncCarenciasLei91 = strToDatetime(syncDict['syncCarenciasLei91'])
                    dateSyncAtuMonetaria = strToDatetime(syncDict['syncAtuMonetaria'])
                    dateSyncSalarioMinimo = strToDatetime(syncDict['syncSalarioMinimo'])
                    dateSyncIpca = strToDatetime(syncDict['syncIpca'])

                    if (datetime.datetime.now() - dateSyncConvMon).days != 0:
                        infoToUpdate[FerramentasEInfo.convMon] = True
                    else:
                        syncJson['syncConvMon'] = syncDict['syncConvMon']

                    if (datetime.datetime.now() - dateSyncTetosPrev).days != 0:
                        infoToUpdate[FerramentasEInfo.tetos] = True
                    else:
                        syncJson['syncTetosPrev'] = syncDict['syncTetosPrev']

                    if (datetime.datetime.now() - dateSyncIndicadores).days != 0:
                        infoToUpdate[FerramentasEInfo.indicadores] = True
                    else:
                        syncJson['syncIndicadores'] = syncDict['syncIndicadores']

                    if (datetime.datetime.now() - dateSyncExpSobrevida).days != 0:
                        infoToUpdate[FerramentasEInfo.expSobrevida] = True
                    else:
                        syncJson['syncExpSobrevida'] = syncDict['syncExpSobrevida']

                    if (datetime.datetime.now() - dateSyncCarenciasLei91).days != 0:
                        infoToUpdate[FerramentasEInfo.carenciasLei91] = True
                    else:
                        syncJson['syncCarenciasLei91'] = syncDict['syncCarenciasLei91']

                    if (datetime.datetime.now() - dateSyncAtuMonetaria).days != 0:
                        infoToUpdate[FerramentasEInfo.atuMonetaria] = True
                    else:
                        syncJson['syncAtuMonetaria'] = syncDict['syncAtuMonetaria']

                    if (datetime.datetime.now() - dateSyncSalarioMinimo).days != 0:
                        infoToUpdate[FerramentasEInfo.salarioMinimo] = True
                    else:
                        syncJson['syncSalarioMinimo'] = syncDict['syncSalarioMinimo']

                    if (datetime.datetime.now() - dateSyncIpca).days != 0:
                        infoToUpdate[FerramentasEInfo.ipca] = True
                    else:
                        syncJson['syncIpca'] = syncDict['syncIpca']

                    loop.run_until_complete(self.atualizaInformacoes(infoToUpdate))

            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))
        else:
            infoToUpdate = {
                FerramentasEInfo.tetos: True,
                FerramentasEInfo.convMon: True,
                FerramentasEInfo.indicadores: True,
                FerramentasEInfo.expSobrevida: True,
                FerramentasEInfo.carenciasLei91: True,
                FerramentasEInfo.atuMonetaria: True,
                FerramentasEInfo.salarioMinimo: True,
                FerramentasEInfo.ipca: True,
            }
            loop.run_until_complete(self.atualizaInformacoes(infoToUpdate))

            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))

    async def atualizaInformacoes(self, infoToUpdate: dict):
        qtdIndicadores = Indicadores.select().count()
        qtdExpSobrevida = ExpSobrevida.select().count()
        qtdTetosPrev = TetosPrev.select().count()
        qtdConvMon = ConvMon.select().count()
        qtdCarenciasLei91 = CarenciaLei91.select().count()
        qtdAtuMonetarias = IndiceAtuMonetaria.select().count()
        qtdSalariosMinimos = SalarioMinimo.select().count()
        qtdIpca = IpcaMensal().select().count()

        asyncTasks = []
        for tipoInfo, sync in infoToUpdate.items():
            if sync:
                if tipoInfo == FerramentasEInfo.tetos:
                    asyncTasks.append(aio.ensure_future(ApiFerramentas().getAllFerramentas(FerramentasEInfo.tetos)))
                elif tipoInfo == FerramentasEInfo.convMon:
                    asyncTasks.append(aio.ensure_future(ApiFerramentas().getAllFerramentas(FerramentasEInfo.convMon)))
                elif tipoInfo == FerramentasEInfo.indicadores:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.indicadores)))
                elif tipoInfo == FerramentasEInfo.expSobrevida:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.expSobrevida)))
                elif tipoInfo == FerramentasEInfo.carenciasLei91:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.carenciasLei91)))
                elif tipoInfo == FerramentasEInfo.atuMonetaria:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.atuMonetaria)))
                elif tipoInfo == FerramentasEInfo.salarioMinimo:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.salarioMinimo)))
                elif tipoInfo == FerramentasEInfo.ipca:
                    asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.ipca)))

        gather = await aio.gather(*asyncTasks)

        tasks: dict = dict(zip(infoToUpdate.keys(), gather))

        for aioTask, infoApi in tasks.items():
            if aioTask == FerramentasEInfo.tetos:
                tetosFromApi: List[dict] = infoApi
                if qtdTetosPrev < len(tetosFromApi):
                    TetosPrev.insert_many(tetosFromApi).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.convMon:
                convMonFromApi: List[dict] = infoApi
                if qtdConvMon < len(convMonFromApi):
                    ConvMon.insert_many(convMonFromApi).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.indicadores:
                indicadoresFromApi: List[dict] = infoApi
                if qtdIndicadores < len(indicadoresFromApi):
                    Indicadores.insert_many(indicadoresFromApi).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.expSobrevida:
                expSobrevidaFromApi: List[dict] = infoApi
                if qtdExpSobrevida < len(expSobrevidaFromApi):
                    ExpSobrevida.insert_many(expSobrevidaFromApi).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.carenciasLei91:
                carenciasLei91FromApi: List[dict] = infoApi
                if qtdCarenciasLei91 < len(carenciasLei91FromApi):
                    CarenciaLei91.insert_many(carenciasLei91FromApi).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.atuMonetaria:
                indicesAtuMonetaria: List[dict] = infoApi
                if qtdAtuMonetarias < len(indicesAtuMonetaria):
                    if len(indicesAtuMonetaria) <= 80:
                        IndiceAtuMonetaria.insert_many(indicesAtuMonetaria).on_conflict('replace').execute()
                    else:
                        listasAAdicionar = divideListaEmPartes(indicesAtuMonetaria, 400)
                        for listaIndice in listasAAdicionar:
                            IndiceAtuMonetaria.insert_many(listaIndice).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.salarioMinimo:
                listaSalarios: List[dict] = infoApi
                if qtdSalariosMinimos < len(listaSalarios):
                    SalarioMinimo.insert_many(listaSalarios).on_conflict('replace').execute()

            elif aioTask == FerramentasEInfo.ipca:
                listaIpca: List[dict] = infoApi
                if qtdIpca < len(listaIpca):
                    IpcaMensal.insert_many(listaIpca).on_conflict('replace').execute()

    def iniciaCampos(self):
        self.lePrimCadLogin.setReadOnly(True)
        self.leNome.setReadOnly(True)
        self.leSobrenome.setReadOnly(True)
        self.leNacionalidade.setReadOnly(True)
        self.leEstadoCivil.setReadOnly(True)
        self.leEmail.setReadOnly(True)

    def loading(self, value: int):
        pass
    #     self.pbarLoading.show()
    #     valor: int = value + self.pbarLoading.value()
    #     self.pbarLoading.setValue(valor)
    #
    #     if valor >= 100:
    #         self.timer.start(500)

    # def escondeLoading(self):
    #     self.pbarLoading.hide()
    #     self.pbarLoading.setValue(0)
    #     self.timer.stop()

    def limpa(self):
        self.leNome.clear()
        self.leSobrenome.clear()
        self.leEmail.clear()
        self.lePrimCadSenha.clear()
        self.leSenhaProvisoria.clear()
        self.leNacionalidade.clear()
        self.leEstadoCivil.clear()
        self.leSenha.clear()
        self.leCdEscritorio.clear()

        self.limpaListaAdv()

    def limpaListaAdv(self):
        for i in reversed(range(self.vlAdv.count())):
            self.vlAdv.itemAt(i).widget().setParent(None)

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
        )

    def apresentandoErros(self, tipoErro):
        if isinstance(tipoErro, ErroConexao):
            if tipoErro == ErroConexao.ConnectionError:
                popUpOkAlerta('Não há conexão com a internet ou com o servidor. \nVerifique se há acesso à internet.')