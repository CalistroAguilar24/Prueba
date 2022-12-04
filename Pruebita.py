#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

#@st.experimental_memo

with st.sidebar:
   st.sidebar.header('Programación avanzada')
   image = Image.open('Logo_Oficial (1).png')
   st.image(image,use_column_width=True)
   selected = option_menu(
      menu_title = 'Menú',
      options = ['Inicio','Informe','Equipo'],
      icons = ['house','book','people'],
      menu_icon = 'cast',
      default_index = 0,
   )
if selected == 'Inicio':
   st.markdown("<h1 style ='text-align: center'> CATALOGO SISMICO 1960-2021 (IGP) </h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.info('La base de datos sobre la actividad sísmica en el país fue realizada por el Instituto Geofísico del Perú (IGP) desde el año de 1960 hasta el 2021. El IGP es la institución responsable del monitoreo de la actividad sísmica del país, y contiene todos aquellos sismos percibidos por la población y registrados por la Red Sísmica Nacional desde 1960, fecha en la que se inicia la vigilancia instrumental de la sismicidad en el Perú.')
   st.write('¿Por qué es importante saber sobre los datos de los sismos?')
   col1, col2 =st.columns(2)
   image = Image.open('imagen 1.jpg')
   col1.write("Los desastres naturales han acompañado el desarrollo de la humanidad a lo largo de la historia; por ello, rescatar y analizar a los sismos desde la historia ayuda a comprender no sólo las acciones humanas en torno a ellos, sino también a descifrar las características y patrones de comportamiento de la actividad sísmica, lo que puede ayudar a los sismólogos, geólogos y otros especialistas a elaborar con mayores datos y precisión, los mapas de riesgo. Además, tener conocimiento sobre estos fenómenos nos permitirá construir una sociedad preventiva, la vulnerabilidad física y la vulnerabilidad social nos ayudará a contar con herramientas –como simulacros y mochilas de emergencia– para estar preparados ante lo que podemos esperar en un evento real.")          
   col2.image(image,use_column_width=True)       
   def download_data():
      url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      filename="Catalogo1960_2021.xlsx"
      urllib.request.urlretrieve(url,filename)
      df=pd.read_csv('Catalogo1960_2021.xlsx')
      return df
   c=download_data()
   st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
   st.dataframe(c)
   st.subheader("Características del Dataset")
   st.write(c.describe())
   
if selected == 'Informe':
   st.markdown("<h1 style ='text-align: center'> CATÁLOGO SÍSMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   selected_year=st.sidebar.selectbox('FECHA_UTC', list(reversed(range(1960,2022))))
   #def download_data():
      #url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      #filename="Catalogo1960_2021.xlsx"
      #urllib.request.urlretrieve(url,filename)
      #df=pd.read_csv('Catalogo1960_2021.xlsx')
      #return df
   #c=download_data()
   #st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
   #st.dataframe(c)
   #st.subheader("Características del Dataset")
   #st.write(c.describe())
	
   #DATOS DE CADA DEPARTAMENTO
   #df_latlog= pd.read_csv('latylog progra.csv')
   #datos_Morropon= pd.read_csv('Morropon_Piura.csv')

   opcion_dataset = st.selectbox('¿Qué dataset deseas visualizar?',('AREQUIPA','Proyectos desaprobados','Proyectos en evaluacion'))
   df_visualizacion = None
   estado = '-'
   datos_Ayabaca= pd.read_csv('Paaaa.csv')
   if opcion_dataset == 'AREQUIPA':
      df_visualizacion = datos_Ayabaca
      estado = 'aprobados'
   #elif opcion_dataset == 'Proyectos desaprobados':
	#df_visualizacion = df_desaprobado
	#estado = 'desaprobados'
   #elif opcion_dataset == 'Proyectos en evaluacion':
	#df_visualizacion = df_evaluacion
	#estado = 'en evaluación'
   t1 = '• Cantidad de cuencas según los '+estado+'' 
   st.dataframe(df_visualizacion)
   #st.subheader(t1)
   #df_cuenca_freq = pd.DataFrame(df_visualizacion["DEPARTAMENTO"].value_counts())
   #st.bar_chart(df_cuenca_freq)
   #st.write('Figura 3. Gráfica del nombre de cuencas en la provincia seleccionada')
   #st.markdown("---")
   



   #url archivo raw
   #url= 'https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv'
   #datos=pd.read_csv(url, sep=',')
   #st.subheader('Gráfico de Epicentro vs Fecha_UTC')
   #st.write('')
   #st.line_chart(data=datos, x='EPICENTRO', y='FECHA_UTC')
   #st.subheader('Gráfico de Magnitud vs Departamento')
   #st.write('')
   #st.line_chart(data=datos, x='MAGNITUD', y='DEPARTAMENTO')
   #st.subheader('Gráfico de Fecha_UTC vs Departamento')
   #st.write('')
   #st.line_chart(data=datos, x='FECHA_UTC', y='DEPARTAMENTO')
   #st.subheader('Gráfico de Profundidad vs Departamento')
   #st.write('')
   #st.line_chart(data=datos, x='PROFUNDIDAD', y='DEPARTAMENTO')
   
   
  
   

if selected == 'Equipo':
   st.markdown("<h1 style ='text-align: center'> ¿Quiénes somos?:</h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.write('Somos un grupo de estudiantes del V ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruano Cayetano Heredia (UPCH). Mediante el procesamiento y visualización de datos se brindará todos los parámetros que caracterizan un sismo con el objetivo de constituirse como una base útil para la realización de estudios en sismología.')
   col1, col2, col3= st.columns(3)
   image1 = Image.open('f238361e-ccb8-48d1-8993-1de25db1c866.jpg')
   col1.header("Miguel Calistro Aguilar")
   col1.image(image1, use_column_width=True)
   image2 = Image.open('WhatsApp Image 2022-11-27 at 23.17.23.jpeg')
   col2.header("Brigytt Contreras Melgar")
   col2.image(image2, use_column_width=True)
   image3 = Image.open('WhatsApp Image 2022-11-28 at 19.18.22.jpeg')
   col3.header("Daniel Chamorro Grados")
   col3.image(image3, use_column_width=True)
   
   

 

