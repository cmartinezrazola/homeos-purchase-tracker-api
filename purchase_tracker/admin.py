from django.contrib import admin
from .models import Marketplace, Order, OrderItem

# 🛒 1. Permite editar los productos directamente dentro de la pantalla de la Orden
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1 # Te deja siempre 1 fila vacía al final para añadir un producto rápido
    fields = ['name', 'brand', 'specs']


# 📦 2. Personalización de la vista de Órdenes
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista general de órdenes
    list_display = ['id', 'created_at', 'marketplace', 'shop', 'shipping', 'total_items']
    
    # Filtros laterales súper cómodos
    list_filter = ['marketplace', 'created_at']
    
    # Buscador para localizar compras rápidamente
    search_fields = ['shop', 'id']
    
    # Inyectamos los productos dentro de la orden
    inlines = [OrderItemInline]

    # 💡 Una columna calculada personalizada para ver cuántos productos tiene la orden
    def total_items(self, obj):
        return obj.order_items.count()
    total_items.short_description = 'Total Itemsx'


# 🌐 3. Registro simple para los Marketplaces
@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name']