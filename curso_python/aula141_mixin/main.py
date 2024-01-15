from log import LogPrintMixin, LogFileMixin

lf = LogFileMixin()
lf.log_error('Something')
lf.log_success('Que legal')

lp = LogPrintMixin()
lp.log_error('Something')
lp.log_success('Que legal')