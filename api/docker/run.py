#!/usr/bin/python

from docker import Client
import json

def get_info():
    try:
        client = Client(base_url='unix://var/run/docker.sock')

        for cli in client.containers(all=True):
            network = list(cli.get('NetworkSettings').get('Networks').keys())[0]

            print('Container: %s' %cli.get('Names')[0][1:])
            print('State: %s' % cli.get('State'))
            print('Status: %s' % cli.get('Status'))
            print('Rede: %s' %network)
            print('IP: %s' %cli.get('NetworkSettings').get('Networks').get(network).get('IPAddress'))
            print('--------------------------------')

            # print(cli)

    except Exception as e:
        print('Fail %s'%e)


if __name__ == '__main__':
    get_info()