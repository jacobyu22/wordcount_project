from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    text = request.GET['full_text']
    split_text = text.split()
    word_count_dict = {}

    for word in split_text:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    sorted_word_list = sorted(word_count_dict.items(),
                              key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',
                  {'full_text': text,
                   'word_count': len(split_text),
                   'word_count_dict': sorted_word_list}
                  )


def about(request):
    return render(request, 'about.html')
