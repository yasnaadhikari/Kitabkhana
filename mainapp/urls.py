from django.urls import path
from mainapp import views, views_ajax
urlpatterns = [
    path('', views.index, name='index'),
    path('genre_books/<genre>', views.genre_books, name='genre_books'),
    path('explore_books/', views.explore_books, name='explore_books'),
    path('book_recommendations/', views.book_recommendations,
         name='book_recommendations'),
    path('library/rated_books', views.read_books, name='read_books'),
    path('library/saved_books', views.SaveList, name='to_read'),
    path('reviews', views.reviews, name='reviews'),
    path('discussion/<int:myid>/', views.discussion, name='discussion'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),


]

# Ajax Views
urlpatterns += [
    path('search_ajax/', views_ajax.search, name='search_ajax'),
    path('book_summary_ajax/', views_ajax.book_summary, name='summary_ajax'),
    path('book_details_ajax/', views_ajax.get_book_details, name='book_details'),
    path('user_rate_book/', views_ajax.user_rate_book, name='user_rate_book'),
    path('add_cart/', views_ajax.add_cart, name='add_cart'),
    path('remove_add_cart/', views_ajax.remove_add_cart, name='remove_add_cart'),
    path('save_book/', views_ajax.save_book, name='save_book'),
    path('remove_saved_book/', views_ajax.remove_saved_book,
         name='remove_saved_book')

]
