from django.conf.urls.defaults import patterns, url

from Books import views

urlpatterns = patterns('',
    # ex: /Books/
    url(r'^$', views.index, name='index'),
    url(r'^adduser/$', views.AddUser, name = 'AddUser'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
	    {'document_root': '/home/benny/public_html/domain1.com/BookBay/media'}),
    url(r'^(?P<user_id>\d+)/$', views.ViewUser, name='ViewUser'),
    url(r'^login/$', views.LogIn, name = 'LogIn'),
    url(r'^logout/$', views.LogOut, name ='LogOut'),
    url(r'^viewbook/(?P<book_id>\d+)/$', views.ViewBook, name = 'ViewBook'),
    url(r'^addbook/$', views.AddBook, name ='AddBook'),
    url(r'^editbook/(?P<bookid>\d+)/$', views.EditBook, name = 'EditBook'),
    url(r'^edituser/$', views.EditUser, name = 'EditUser'),
    url(r'^removebook/(?P<bookid>\d+)/$', views.RemoveBook, name = 'RemoveBook'),
    url(r'^auctionsetup/(?P<bookid>\d+)/$', views.AuctionSetup, name = 'AuctionSetup'),
    url(r'^auction/(?P<auctionid>\d+)/$', views.Auction, name = 'Auction'),
    url(r'^salesetup/(?P<bookid>\d+)/$', views.SaleSetup, name = 'SaleSetup'),
    url(r'^pay/(?P<_type>\d)/(?P<_id>\d+)/$',views.PaySale, name = 'PaySale'),
    url(r'^sale/(?P<saleid>\d+)/$', views.Sale, name = 'Sale'),
    url(r'^auctionbook/(?P<bookid>\d+)/$', views.AuctionBook, name = 'AuctionBook'),
    url(r'^salebook/(?P<bookid>\d+)/$', views.SaleBook, name = 'SaleBook'),
    url(r'^notverified/$', views.NotVerified, name = 'NotVerified'),
    url(r'^deleteauction/(?P<auctionid>\d+)/$', views.DelAuction, name = 'DelAuction'),
    url(r'^rate/(?P<userid>\d+)/$', views.RateUser, name = 'RateUser'),
    url(r'^deletesale/(?P<saleid>\d+)/$', views.DelSale, name = 'DelSale'),
    url(r'^usercomment/(?P<userid>\d+)/$', views.UserComment, name = 'UserComment'),
    url(r'^bookcomment/(?P<bookid>\d+)/$', views.BookComment, name = 'BookComment'),
    url(r'^getpoints/$', views.GetPoints, name = 'GetPoints'),
    url(r'^browse/$', views.Browse, name = 'Browse'),
    url(r'^search/$', views.Search, name = 'Search'),
    url(r'^password/$', views.ChangePassWord, name = 'ChangePassWord'),
    url(r'^usercomplaint/(?P<userid>\d+)/$', views.UserComplaints, name = 'UserComplaints'),
    url(r'^bookcomplaint/(?P<bookid>\d+)/$', views.BookComplaint, name = 'BookComplaint'),
    url(r'^ratebook/(?P<bookid>\d+)/$', views.RateBook, name = 'RateBook'),
    url(r'^endsale/(?P<saleid>\d+)/$', views.EndSale, name = 'EndSale'),
)