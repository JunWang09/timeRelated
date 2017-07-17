us_tclaim_2000['pol_eff_dt'] = pd.to_datetime(us_tclaim_2000.pol_effective_dt,format='%d%b%Y')
us_tclaim_2000['diff'] = (us_tclaim_2000['acc_dt'] - us_tclaim_2000['pol_eff_dt'])/np.timedelta64(1,'D') 

us_tclaim_2000['valuation_date'] = us_tclaim_2000.apply(lambda x: x['pol_eff_dt'] + dt.timedelta(days=x['days']), axis=1)


