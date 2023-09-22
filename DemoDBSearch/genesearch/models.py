from django.db import models

# Create your models here.


class Yellow(models.Model):
    Chr=models.CharField(max_length=200)
    Start=models.IntegerField()
    End=models.IntegerField()
    Ref=models.CharField(max_length=10)
    Alt=models.CharField(max_length=10)
    Ref_Gene=models.CharField(max_length=200)
    Func_refGene=models.CharField(max_length=200)
    ExonicFunc_refGene=models.CharField(max_length=200)
    OMIM=models.IntegerField()
    

    def __str__(self):
        return self.Ref_Gene

class Green(models.Model):
    
    dbSNP_ID=models.CharField(max_length=200)
    ClinVar_Sig=models.CharField(max_length=200)
    Ref_Gene = models.CharField(max_length=200)
    InterVa_InterVar_and_Evidence=models.CharField(max_length=1000)
    Freq_gnomAD_genome_ALL=models.CharField(max_length=200)
    Freq_esp6500siv2_all=models.CharField(max_length=200)
    Freq_1000g2015aug_all=models.CharField(max_length=200)
    CADD_raw=models.CharField(max_length=200)
    CADD_phred=models.CharField(max_length=200)
    SIFT_score=models.CharField(max_length=200)

    # yellow=models.ForeignKey(Yellow,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.dbSNP_ID

