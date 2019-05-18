from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['text']
    list=text.split(' ')
    len(list)
    word_count={}
    count=0
    
    for w in list:
        if w in word_count:
            word_count[w]+=1
        else:
            word_count[w]=1

    for i in text:
        if i not in [' ']:
            count+=1

    context={
        "full":text,
        "total":len(list),
        "word_count":word_count,
        "count":count,
    }
    return render(request,'result.html',context)
