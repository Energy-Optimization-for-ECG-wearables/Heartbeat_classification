import wfdb
from wfdb import processing

# sig, fields = wfdb.rdsamp(".data/physionet.org/files/mitdb/1.0.0/234", channels=[0])
# xqrs = processing.XQRS(sig=sig[:,0], fs=fields['fs'])
# xqrs.detect()

# wfdb.plot_items(signal=sig, ann_samp=[xqrs.qrs_inds])

record_number: str = "234"

record = wfdb.rdrecord(
    '.data/physionet.org/files/mitdb/1.0.0/' + record_number, sampto=3000)

print("sampling freq : %f" % record.fs)
print("signal length : %d" % record.sig_len)
# print the first few lines of the annotation file
print(record.__dict__)

annotation = wfdb.rdann(
    '.data/physionet.org/files/mitdb/1.0.0/' + record_number, 'atr', sampto=3000)

wfdb.plot_wfdb(record=record, annotation=annotation, plot_sym=True,
               time_units='seconds', title='MIT-BIH Record ' + record_number + ' from PhysioNet',
               figsize=(10, 4), ecg_grids='all')
