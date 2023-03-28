# 모델 참고

from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    journalist = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

# 1.
Newspaper.objects.get(pk=1).journalist

# 2.
Newspaper.objects.filter(journalist='Laney Mccullough').count()

# 3. 
Newspaper.objects.order_by('-pk')

# 4.
Newspaper.objects.order_by('-created_at')

# 5.
Newspaper.objects.filter(journalist__contains='Britney').count()

# 6.
Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()

# 7.
Newspaper.objects.filter(created_at__date__gt='1999-12-31').count()

# 8.
lastpaper = Newspaper.objects.values().last()
for k,v in lastpaper.items():
    if k in ['title', 'content', 'journalist']:
        print(k, ':' , v)


# 기타 orm 코드

# 1. 슬라이싱
Newspaper.objects.all()[:3]
# ~3개까지 조회

Newspaper.objects.all()[2:5]
# 3~5 조회

Newspaper.objects.all()[:5]
# 1~5 조회 


# 2. 제외하고 조회
Newspaper.objects.exclude(pk=1)
# id 1 을 제외하고 조회됨
Newspaper.objects.exclude(journalist='Laney Mccullough')
# journalist가 Laney Mccullough 인 object를 제외 하고 조회됨


# 3. 대소문자를 구분하지 않고 특정 문자가 포함된 것을 찾을 때
Newspaper.objects.filter(journalist__icontains='BRITNEY').count()
# Newspaper.objects.filter(journalist__contains='Britney').count() 와 똑같은 결괏값 799 반환


# 4. created_at 필드가 2000-01-01 이전 데이터 개수 조회
Newspaper.objects.filter(created_at__date__lt='2000-01-01').count()


# 5. crated_at 필드에서 year 가 2001 년 인 것 만 조회
Newspaper.objects.filter(created_at__year='2001')
# __month, __day, __date 도 가능 / __date 는 YY-MM-DD 형식