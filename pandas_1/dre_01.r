df.main <- read.csv(
    fileEncoding = 'latin1',             
    na.strings = c('NA', ''),           
    file = 'razao_jan.csv',    
    sep = ';',                                                     
)

print(str(df.main))