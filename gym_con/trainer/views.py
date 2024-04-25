from django.shortcuts import render
from . models import Trainer , Category , Tag



def trainer_list(request):
    trainers = Trainer.objects.all().order_by
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context= {
        'trainers' : trainers ,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'trainer.html', context)




def trainer_detail(request, category_slug, trainer_id):
    trainer = Trainer.objects.get(category__slug=category_slug , id = trainer_id)


    context={
        'trainer': trainer 
        
    }
    return render(request, 'trainers.html', context)




def category_detail(request, category_slug,):
    trainers = Trainer.objects.all().filter(category__slug= category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context={
        'trainers': trainers ,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'trainer.html', context)




def tag_detail(request, tag_slug,):
    trainers = Trainer.objects.all().filter(tags__slug= tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context={
        'trainers': trainers ,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'trainer.html', context)