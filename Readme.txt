*************************************************************************************************************************
*															*
*					B�LG�SAYAR A� TEKNOLOJ�LER� �DEV-1-						*
*						ABDULLAH KAYAHAN							*
*															*
*************************************************************************************************************************
*															*
*	Proje Dosyalar�: 												*
*		1- server.py: Server ba�lant�s�n�n yap�ld��� dosyam�zd�r. Bu dosya bir port a�arak dinlemeye ba�lar.	*
*		     siniflar.py isimli dosyada bulunan Selection,Room ve User s�n�flar�n� kullanarak multiple		*
*		     chat room'a izin verir.										*
*		2- siniflar.py: Server dosyas�nda kullan�lacak olan s�n�flar�n tan�mland��� dosyad�r. As�l i� bu 	*
*		     dosyadaki s�n�flar �zerinde d�nmektedir. Men� i�lemleri, kullan�c� girisi, oda se�me ve benzeri 	*	
*		     i�lemler bu dosya �zerinde tan�mlanm��t�r.								*
*		3- client.py:  Kullan�c�lar�n servera ba�lanmak i�in kullanaca�� dosyad�r. Bu dosya �al��t�r�l�rken	*
*		     hostname ve port numaras� parametre olarak verilmelidir.						*	
*	Dosyalar�n �al��t�r�lmas�:											*
*		server.py ---> terminal ekran�na "python server.py"  yaz�l�p enter'a bas�lmas� yeterlidir.		*
*		siniflar.py ---> bu dosyay� her hangi bir terminalde �al��t�rmaya gerek yoktur. Bu dosya server.py 	*
*		 dosyas� i�inden �a�r�lacakt�r.										*
*		client.py ---> Terminal Ekran�na "python client.py 127.0.0.1 5000" yaz�larak �al��t�r�lmal�d�r.		*
*			Ard�ndan men� ekran� kullan�c�ya g�sterilecektir. 						*
*			Giri� yapmak i�in "<giris> kullan�c�_Adi sifre"  yaz�l�p entera bas�l�r.			*
*			Kay�t yapmak i�in "<kayit> kullanici_adi sifre"  yaz�p entera bas�l�r.				*
*			Chat odalar�n� listelemek i�in "<listele>" yaz�l�p entera bas�l�r.				*
*			Bir odaya girmek i�in "<katil> oda_Adi" yazilip entera bas�l�r.					*
*															*
*************************************************************************************************************************		
