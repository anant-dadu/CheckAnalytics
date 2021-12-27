
import os
import re
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q7XG1LL6VG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q7XG1LL6VG');
</script>"""
import streamlit as st
# a=os.path.dirname(st.__file__)+'/static/index.html'
#with open(a, 'r') as f:
#     data=f.read()
    # if len(re.findall('G-', data))==0:
#    if not 'G-' in data:
#        with open(a, 'w') as ff:
#            newdata=re.sub('<head>','<head>'+code,data)
#            ff.write(newdata)
            

# st.write(data)
st.write(st.__file__)
st.write(os.listdir(os.path.dirname(st.__file__)))
st.write(os.listdir(os.path.dirname(st.__file__) + '/static'))
st.write(os.listdir(os.path.dirname(st.__file__) + '/static/static'))

            
google_analytics_js = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q7XG1LL6VG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-Q7XG1LL6VG', {'cookieDomain': 'none', 'checkProtocolTask':  null });
  
</script>
    """
google_analytics_js = """
<!-- Default Statcounter code for My Testing Website
https://share.streamlit.io/anant-dadu/checkanalytics -->
<script type="text/javascript">
var sc_project=12694448; 
var sc_invisible=0; 
var sc_security="d344aa44"; 
var scJsHost = "https://";
document.write("<sc"+"ript type='text/javascript' src='" + scJsHost+
"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="Web Analytics"
href="https://statcounter.com/" target="_blank"><img class="statcounter"
src="https://c.statcounter.com/12694448/0/d344aa44/0/" alt="Web Analytics"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code -->
"""
# google_analytics_js = """<a title="Real Time Web Analytics" href="http://clicky.com/101347652"><img alt="Clicky" src="//static.getclicky.com/media/links/badge.gif" border="0" /></a>
# <script async src="//static.getclicky.com/101347652.js"></script>
# <noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/101347652ns.gif" /></p></noscript>"""
# st.components.v1.html(google_analytics_js)
st.write("Hello How are you")
if st.button("Click"):
  st.write("Welcome")
  
google_analytics_js = """<script async src="//static.getclicky.com/101347652.js"></script>
<noscript><p><img alt="Clicky" width="1" height="1" src="//in.getclicky.com/101347652ns.gif" /></p></noscript>"""
st.components.v1.html(google_analytics_js)
