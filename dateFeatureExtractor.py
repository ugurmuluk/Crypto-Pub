
import numpy as np

def dateExtractor(x):
    years = x.astype('datetime64[Y]').astype(int) + 1970
    months = x.astype('datetime64[M]').astype(int) % 12 + 1
    daysOfTheYear = x.astype('datetime64[D]').astype(int) - 365 * (years - 1970) - 12
    daysOfTheYear = np.digitize(daysOfTheYear, [0, 60, 120, 180, 240, 300, 360])
    businessDays = np.is_busday(x.astype('datetime64[D]'))
    businessDays = businessDays.astype(int)
    hours = np.mod(x.astype('datetime64[h]').astype(int) - 395659, 24)
    dayOfTheWeek = np.mod((x.astype('datetime64[D]').astype(int)), 7)
    years = years.astype('int64')
    months = months.astype('int64')
    hourPeriod = np.digitize(hours, [0, 12, 24])

    return years, months, daysOfTheYear, businessDays, hours, dayOfTheWeek, hourPeriod

