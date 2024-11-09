import pandas as pd


igs_data = {
    'Location': 'Jl. mayor salim',
    'Operating Hours': '7 AM - 17:00 PM',
    'Facilities': ['Cafetaria', 'Swimming pool', 'Hall']
}

kumbang_data = {
    'Location': 'Jl. abdul rozak',
    'Operating Hours': '7:00 AM - 17:00 PM',
    'Facilities': ['Basket ball course', 'Swimming pool', 'Kitchen']
}

Xaverius1_data = {
    'Location': 'Jl.Bangau',
    'Operating Hours': '7:00 AM - 17:00 PM',
    'Facilities': ['Canteen', 'Basketball course', 'Football course']
}

Sph_data = {
    'Location': 'Jl.Pakjo',
    'Operating Hours': '7:00 AM - 17:00 PM',
    'Facilities': ['Cafetaria', 'Basketball course', 'Library']
}

sis_data = {
    'Location': 'Jl. Letda Abdul rozak',
    'Operating Hours': '7:00 AM - 17:00 PM',
    'Facilities': ['Cafetaria', 'PlayGround', 'Library']
}

Baptis_data = {
    'Location': 'Jl. Sudirman',
    'Operating Hours': '7:00 AM - 17:00 PM',
    'Facilities': ['Cafetaria', 'library', 'Baskertball course']
}

df = pd.DataFrame([igs_data, kumbang_data, Xaverius1_data,Sph_data,sis_data,Baptis_data], 
index=['IGS', 'KUMBANG','XAVERIUS1','SPH','SIS','BAPTIS'])


print(df)