def get_population(country_dic):
  population_dic ={
    '2022':country_dic['2022 Population'],
    '2020':country_dic['2020 Population'],
    '2015':country_dic['2015 Population'],
    '2010':country_dic['2010 Population'],
    '2000':country_dic['2000 Population'],
    '1990':country_dic['1990 Population'],
    '1980':country_dic['1980 Population'],
    '1970':country_dic['1970 Population'],
  }
  return population_dic.keys(),population_dic.values()

def list_by_country(data, pais):
  result = list(filter(lambda item : item['pais'] == pais, data))
  return result