"""Justice_For_All URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home_page.views import homepage
from signup.views import signaction
from login.views import loginaction
from logout.views import logoutaction
from contact.views import contact
from gallery.views import gallery
from sin.views import sin 
from sout.views import sout
from sup.views import sup
from about_us.views import about_us
from advocate.views import advocate
from solution.views import solution
from AFAP.views import AFAP
from AFAPP.views import AFAPP
from AFBC.views import AFBC
from AFNC.views import AFNC
from AR.views import AR
from BFL.views import BFL
from BOCC.views import BOCC
from CA.views import CA
from CBN.views import CBN
from CIGST.views import CIGST
from CIIEC.views import CIIEC
from CM.views import CM
from CITA.views import CITA
from COGST.views import COGST
from CRLA.views import CRLA
from CRR.views import CRR
from DACC.views import DACC
from DC.views import DC
from DIPPC.views import DIPCC
from Dis.views import Dis
from Disco.views import Disco
from DOPF.views import DOPF
from DSC.views import DSC
from EC.views import EC
from ESIF.views import ESIF
from ESIR.views import ESIR
from F.views import F
from FA.views import FA
from FARFYPLC.views import FARFYPLC
from FATO.views import FATO
from FCA.views import FCA
from FLA.views import FLA
from FraA.views import FraA
from GAFAL.views import GAFAL
from GBLA.views import GBLA
from GBLO.views import GBLO
from GC.views import GC
from GD.views import GD
from GSTR.views import GSTR
from Hearing.views import Hearing
from IECR.views import IECR
from IP.views import IP
from ISOR.views import ISOR
from ITA.views import ITA
from JVA.views  import JVA
from LA.views import LA
from LALA.views import LALA
from LLPR.views import LLPR
from LN.views import LN
from LoanAgre.views import LoanAgre
from LTI.views import LTI
from LUTA.views import LUTA
from LWFR.views import LWFR
from MA.views import MA
from MD.views import MD
from MOS.views import MOS
from MOT.views import MOT
from MOU.views import MOU
from MSA.views import MSA
from NDA.views import NDA
from NIDGICR.views import NIDGICR
from OPCR.views import OPCR
from PAPOA.views import PAPOA
from PFAESIF.views import PFAESIF
from PFAESIR.views import PFAESIR
from PFF.views import PFF
from PFR.views import PFR
from PFreg.views import PFreq
from PLCR.views import PLCR
from PLCWIAFS.views import PLCWIAFS
from PostDisc.views import PostDisc
from POW.views import POW
from PP.views import PP
from PR.views import PR
from PreFili.views import PreFili
from PRS.views import PRS
from PS.views import PS
from PSA.views import PSA
from PTF.views import PTF
from PTFD.views import PTFD
from PTFE.views import PTFE
from PTR.views import PTR
from RANBFCCII.views import RANBFCCII
from RATSGBAI.views import RATSGBAI
from RC.views import RC
from RelChan.views import RelChan
from RTATO.views import RTATO
from SAEAR.views import SAEAR
from SCR.views import SCR
from SD.views import SD
from SHA.views import SHA
from SOAICII.views import SOAICII
from SPA.views import SPA
from SR.views import SR
from SSIMSMER.views import SSIMSMER
from TAN.views import TAN
from TLR.views import TLR
from TMW.views import TMW
from TOS.views import TOS
from TOSAPP.views import TOSAPP
from TOT.views import TOT
from TR.views import TR
from TRADErenew.views import TRADErenew
from Trial.views import Trial
from TS.views import TS
from TW.views import TW
from USACC.views import USACC
from USACI.views import USACI
from VA.views import VA
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('sign_out/', logoutaction),
    path('home_page/', homepage),
    path('contact/', contact ),
    path('gallery', gallery),
    path('about_us/', about_us),
    path('advocate/', advocate),
    path('solution/', solution),
    path('sup/',sup),
    path('sin/',sin),
    path('sout/',sout),
    path('AFAP/',AFAP),
    path('AFAPP/', AFAPP),
    path('AFBC/', AFBC),
    path('AFNC/', AFNC),
    path('AR/', AR),
    path('BFL/',BFL),
    path('BOCC/', BOCC),
    path('CA/',CA),
    path('CBN/',CBN),
    path('CIGST/',CIGST),
    path('CIIEC/',CIIEC),
    path('CITA/',CITA),
    path('CM/',CM),
    path('COGST/',COGST),
    path('CRLA/',CRLA),
    path('CRR/',CRR),
    path('DACC/',DACC),
    path('DC/',DC),
    path('DIPCC/',DIPCC),
    path('Dis/',Dis),
    path('Disco/',Disco),
    path('DOPF/',DOPF),
    path('DSC/',DSC),
    path('EC/',EC),
    path('ESIF/',ESIF),
    path('ESIR/', ESIR),
    path('F/',F),
    path('FA/',FA),
    path('FAREYPLC/',FARFYPLC),
    path('FATO/',FATO),
    path('FCA/',FCA),
    path('FLA/',FLA),
    path('FraA/',FraA),
    path('GAFAL/',GAFAL),
    path('GBLA/',GBLA),
    path('GBLO/',GBLO),
    path('GC/',GC),
    path('GD/',GD),
    path('GSTR/',GSTR),
    path('Hearing/',Hearing),
    path('IECR/',IECR),
    path('IP/',IP),
    path('ISOR/',ISOR),
    path('ITA/',ITA),
    path('JVA/',JVA),
    path('LA/',LA),
    path('LALA/',LALA),
    path('LLPR/',LLPR),
    path('LN/',LN),
    path('LoanAgre/',LoanAgre),
    path('LTI/',LTI),
    path('LUTA/',LUTA),
    path('LWFR/',LWFR),
    path('MA/',MA),
    path('MD/',MD),
    path('MOS/',MOS),
    path('MOT/',MOT),
    path('MOU/',MOU),
    path('MSA/',MSA),
    path('NDA/',NDA),
    path('NIDGICR/',NIDGICR),
    path('OPCR/',OPCR),
    path('PAPOA/',PAPOA),
    path('PFAESIF/',PFAESIF),
    path('PFAESIR/',PFAESIR),
    path('PFF/',PFF),
    path('PFR/',PFR),
    path('PFreq/',PFreq),
    path('PLCR/',PLCR),
    path('PLCWIAFS/',PLCWIAFS),
    path('PostDisc/',PostDisc),
    path('POW/',POW),
    path('PP/',PP),
    path('PR/',PR),
    path('PreFili/', PreFili),
    path('PRS/',PRS),
    path('PS/',PS),
    path('PSA/',PSA),
    path('PTF/',PTF),
    path('PTFD/',PTFD),
    path('PTFE/',PTFE),
    path('PTR/',PTR),
    path('RANBFCCII/',RANBFCCII),
    path('RATSGBAI/',RATSGBAI),
    path('RC/',RC),
    path('RelChan/',RelChan),
    path('RTATO/',RTATO),
    path('SAEAR/',SAEAR),
    path('SCR/',SCR),
    path('SD/',SD),
    path('SHA/',SHA),
    path('SOAICII/',SOAICII),
    path('SPA/',SPA),
    path('SR/',SR),
    path('SSIMSMER/',SSIMSMER),
    path('TAN/',TAN),
    path('TLR/',TLR),
    path('TMW/',TMW),
    path('TOS/',TOS),
    path('TOSAPP/',TOSAPP),
    path('TOT/',TOT),
    path('TR/',TR),
    path('TRADErenew/',TRADErenew),
    path('Trial/', Trial),
    path('TS/',TS),
    path('TW/',TW),
    path('USACC/',USACC),
    path('USACI/',USACI),
    path('VA/',VA),
    path('', include('authentication.urls')),
    path('', include('contact.urls')),
    path('', include('advocate_authentication.urls')),
]
