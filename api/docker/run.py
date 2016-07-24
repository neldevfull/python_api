# -*- coding: utf-8 -*-

from docker import Client


class DockerManager:
    def __init__(self):
        try:
            self.client = Client(base_url='unix://var/run/docker.sock')
        except Exception as e:
            print('Fail %s' %e)

    def inspect_container(self, container_id):
        try:
            print(self.client.inspect_container(container_id))
        except Exception as e:
            print('Fail %s' %e)

    def create_container(self, name, hostname, image):
        try:
            self.client.create_container(
                name=name,
                hostname=hostname,
                image=image,
                command='/bin/bash',
                detach=True,
                stdin_open=True,
                tty=True
            )
        except Exception as e:
            print('Fail %s' %e)

    def print_container(self, container):
        network = list(container.get('NetworkSettings').get('Networks').keys())[0]

        print('Container: %s' %container.get('Names')[0][1:])
        print('State: %s' % container.get('State'))
        print('Status: %s' % container.get('Status'))
        print('Rede: %s' %network)
        print('IP: %s' %container.get('NetworkSettings').get('Networks').get(network).get('IPAddress'))
        print('--------------------------------')

    def get_containers(self):
        try:
            for cli in self.client.containers(all=True):
                self.print_container(cli)

        except Exception as e:
            print('Fail %s' %e)