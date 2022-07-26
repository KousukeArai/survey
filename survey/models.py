from django.db import models

# class Grade(models.Model):
#     name = models.CharField(verbose_name='学年', max_length=10)
    
#     class Meta:
#         verbose_name_plural = "学年"

#     def __str__(self):
#         return self.name


# class Questions(models.Model):
#     grade = models.ForeignKey(Grade, verbose_name='学年', related_name='q_grade', on_delete=models.CASCADE)
#     text = models.CharField(verbose_name='問題', max_length=20)
#     ans = models.CharField(verbose_name='正解', max_length=10)
    
#     class Meta:
#         verbose_name_plural = "問題"

#     def __str__(self):
#         return self.text

# class Answers(models.Model):
#     question = models.ForeignKey(Questions, verbose_name='問題番号', related_name='ans_q', on_delete=models.CASCADE)
#     ans_num = models.IntegerField(verbose_name="回答番号")
#     name = models.CharField(verbose_name='回答', max_length=10)
    
#     class Meta:
#         verbose_name_plural = "回答"

#     def __str__(self):
#         return self.name