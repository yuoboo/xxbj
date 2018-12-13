# encoding=utf-8
import yaml


def yaml_obj():
    obj = yaml.load("""
    - hosts: webservers
      vars:
        worker_pro: 4
        num_cpus: 4
        root: /data
      remote_user: root
      tasks:
      - name: this is name
        yum: pkg=nginx state=latest
      - name: write
        template: src=/home/test/ansible/nginx/nginx2.conf dest=/etc/nginx/nginx.conf
        notify:
        - restart: nginx
      handlers:
        - name: restart nginx
          service: name=nginx state=restarted

    """)
    print obj


def test_yaml():
    f = open("test_yaml.yaml", 'r')
    obj = yaml.load(f)
    print obj


if __name__ == '__main__':
    # yaml_obj()
    test_yaml()
