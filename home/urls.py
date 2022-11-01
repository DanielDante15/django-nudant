from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('enderecos',views.EnderecoViewSet,basename='enderecos')
router.register('clientes',views.ClienteViewSet,basename='clientes')
router.register('contas',views.ContaViewSet,basename='contas')
router.register('cartoes',views.CartaoViewSet,basename='cartoes')
router.register('faturas',views.FaturaViewSet,basename='faturas')
router.register('transacoes',views.TransacaoViewSet,basename='transacoes')
router.register('emprestimos',views.EmprestimoViewSet,basename='emprestimos')
router.register('pagamento_emprestimos',views.PagEmprestimoViewSet,basename='pagamento_emprestimo')
router.register('favoritos',views.FavoritosViewSet,basename='favoritos')
router.register('extratos',views.ExtratoViewSet,basename='extratos')



urlpatterns = router.urls
