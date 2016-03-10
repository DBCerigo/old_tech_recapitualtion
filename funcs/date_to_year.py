

def d_to_y(col):
    return col.map(lambda x: int(x[:4]))

# Date to years function - works on application date and publication date in one
def date_to_year(df):
    if 'appln_filing_date' in df.columns:
        df.appln_filing_date = df.appln_filing_date.map(lambda x: int(x[:4]))
        df.rename(columns={'appln_filing_date': 'app_year'}, inplace=True)
    if 'publn_date'in df.columns:
        df.publn_date = df.publn_date.map(lambda x: int(x[:4]))
        df.rename(columns={'publn_date': 'pub_year'}, inplace=True)
    return
