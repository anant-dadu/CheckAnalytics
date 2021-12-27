import streamlit as st

code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q7XG1LL6VG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q7XG1LL6VG');
</script>"""

a=os.path.dirname(st.__file__)+'/static/index.html'
with open(a, 'r') as f:
    data=f.read()
    if len(re.findall('G-', data))==0:
        with open(a, 'w') as ff:
            newdata=re.sub('<head>','<head>'+code,data)
            ff.write(newdata)
            
            
            
st.write("Hello How are you")
if st.button("Click"):
  st.write("Welcome")
