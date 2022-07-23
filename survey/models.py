from django.db import models

class Grade(models.Model):
    name = models.CharField(verbose_name='学年', max_length=10)
    
    class Meta:
        verbose_name_plural = "学年"

    def __str__(self):
        return self.name


class Questions(models.Model):
    grade = models.ForeignKey(Grade, verbose_name='学年', related_name='q_grade', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='学年', max_length=20)
    se1 = models.CharField(verbose_name='選択肢1', max_length=10)
    se2 = models.CharField(verbose_name='選択肢2', max_length=10)
    se3 = models.CharField(verbose_name='選択肢3', max_length=10)
    se4 = models.CharField(verbose_name='選択肢4', max_length=10)
    ans = models.CharField(verbose_name='正解', max_length=10)
    
    class Meta:
        verbose_name_plural = "問題"

    def __str__(self):
        return self.text
