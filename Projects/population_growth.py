#Conversions to seconds
second_min=60
min_hour=60
hour_day=24
day_year=365

#inputs
curr_pop=380123456
born_t=6                #Every 6 seconds new born
die_t=12                #Every 12 seconds one person dies
immi_t=40               #Every 40 seconds 1 person immigrates

time_s= second_min*min_hour*hour_day*day_year  #total seconds/year

def in_out(time,born_t,die_t,immi_t):
    born=(time/born_t)
    die=(time/die_t)
    immi=(time/immi_t)

    sum=born-die+immi
    return sum

gain_year=in_out(time_s,born_t,die_t,immi_t)
final_sum= curr_pop + 3*(gain_year)

print("The population 3 years after is:",final_sum)


