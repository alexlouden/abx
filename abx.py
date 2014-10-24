#!/usr/bin/env python
from __future__ import division
import sys
from csv import DictWriter
from subprocess import PIPE, Popen
from cStringIO import StringIO


class TestResult(object):

    @classmethod
    def parse(cls, result):
        x = TestResult()

        # Parse lines to dictionary of data
        data = {}
        for line in result.splitlines():
            try:
                k, v = line.split(': ', 1)
                v = v.strip()
                data[k] = v
            except ValueError:
                pass

        # Set attributes
        x.concurrency = int(data['Concurrency Level'])
        x.num_requests = int(data['Complete requests'])
        x.failed_requests = int(data['Failed requests'])
        x.time_taken = float(data['Time taken for tests'].split()[0])

        try:
            x.transfer_rate = float(data['Transfer rate'].split()[0])

            x.total_mean = float(data['Total'].split()[1])
            x.total_median = float(data['Total'].split()[3])
            x.total_max = float(data['Total'].split()[4])

        except KeyError:
            # No results
            x.transfer_rate = 0
            x.total_mean = 0
            x.total_median = 0
            x.total_max = 0

        try:
            x.percentage_failed = x.failed_requests / x.num_requests
        except ZeroDivisionError:
            x.percentage_failed = 0

        return x

    def to_dict(self):
        return dict(self.__dict__)


def print_results(results):
    dict_results = [r.to_dict() for r in results]
    fieldnames = ['concurrency', 'total_mean', 'total_median', 'total_max', 'percentage_failed']

    f = StringIO()
    writer = DictWriter(f, fieldnames, restval='', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(dict_results)

    f.seek(0)
    print '\n'
    print f.read()


def run_test(time, url):

    results = []

    for c in [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]:
        data = run_ab(c, time, url)
        result = TestResult.parse(data)
        results.append(result)

    print_results(results)
    return results


def run_ab(c, t, url):
    command = ['ab', '-c', str(c), '-t', str(t), url]
    print 'running {}'.format(' '.join(command))
    return run_command(command)


def run_command(command):
    pipe = Popen(command, bufsize=-1, stdout=PIPE)
    return pipe.communicate()[0]


def print_usage():
    print 'Usage: abx.py time url'
    print 'time - number of seconds to run each test'
    print 'url - site to test'
    sys.exit()

if __name__ == '__main__':
    try:
        time = sys.argv[1]
    except KeyError:
        print_usage()

    try:
        url = sys.argv[2]
    except KeyError:
        print_usage()

    data = run_test(time, url)
