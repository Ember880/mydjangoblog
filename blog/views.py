from datetime import date
from django.shortcuts import render

# Create your views here.

posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Bright",
        "date": date(2023, 6, 7),
        "title":"Mountain Hiking",
        "excerpt":"jafgjh ionkjabfui befhjathejhtheksuafhbsiinf siund g;oo;f than ena",
        "content":"""jklafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabs
            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljab

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabkgsdjgnosagn;ogdsovm]]
            """,
 },


         {
        "slug":"School vibes",
        "image":"schoolboy.jpg",
        "author":"Nobody",
        "date": date(2023,3, 9),
        "title":"Scool is just fine",
        "excerpt":"jafgjh ionkjabfui befhjathejhtheksuafhbsiinf siund g;oo;f than ena",
        "content":"""jklafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabs
            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljab

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabkgsdjgnosagn;ogdsovm]]
            """,
 
 },

     {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Bright",
        "date": date(2023, 6, 7),
        "title":"Mountain Hiking",
        "excerpt":"jafgjh ionkjabfui befhjathejhtheksuafhbsiinf siund g;oo;f than ena",
        "content":"""jklafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabs
            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljab

            klafjflkfjijgoanueri; hvibiehpr;onfsjd;ondskjgbgnodasnewq'[fijkvmpvk]klmlvs
            anfeisdagvildsabhsd;bkjdsbvicnvndgpgjgnpiuadkvjnnlknabduyvhjahfoovnd vogogja[agonok
            kjablghugpgha;ongsdaggnon[ognsojg'kmsg
            jdhfaushgdngjas;aghu9gn;kjgaphkljabkgsdjgnosagn;ogdsovm]]
            """,
 }
]

def get_date(post):
    return post["date"]d

def starting_page(request):
    sorted_posts =posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-post.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")