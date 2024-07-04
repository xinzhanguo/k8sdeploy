# k8sdeploy
deploy a k8s cluster step by step


k8s+containerd


https://kubernetes.io/

## init nodes

```
init.sh
```

## certs
```
python gen.py ca-config.json ca.yaml
cfssl gencert -initca ca-csr.json | cfssljson -bare ca
cfssl gencert \
    -ca=ca.pem \
    -ca-key=ca-key.pem \
    -config=ca-config.json \
    -profile=kubernetes etcd-csr.json | cfssljson -bare etcd

cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes admin-csr.json | cfssljson -bare admin

```
## https://github.com/easzlab/kubeasz/blob/master/docs/setup/01-CA_and_prerequisite.md
* 生成 admin 用户证书
* 生成 ~/.kube/config 配置文件
* 生成 kube-proxy.kubeconfig 配置文件


```
https://dl.k8s.io/release/stable.txt

https://dl.k8s.io/v1.30.2/bin/linux/amd64/apiextensions-apiserver
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-aggregator
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-apiserver
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-controller-manager
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-log-runner
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-proxy
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kube-scheduler
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kubeadm
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kubectl
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kubectl-convert
https://dl.k8s.io/v1.30.2/bin/linux/amd64/kubelet
https://dl.k8s.io/v1.30.2/bin/linux/amd64/mounter
```




## etcd
```
etcd.sh
```

## register
https://hub.docker.com/_/registry

## containerd
```
https://github.com/containerd/cri/blob/master/docs/installation.md

tar zxvf cri-containerd-cni-1.7.18-linux-amd64.tar.gz -C /
```
/etc/containerd/config.toml
change:
```
    sandbox_image = "private.register/google_containers/pause:3.8"
[plugins."io.containerd.grpc.v1.cri".registry.mirrors."private.register"]
  endpoint = ["http://private.register"]
```

## api server
```
api.sh
```

## manager
```
#manager.sh
- name: 创建 kube-controller-manager证书与私钥
cfssl gencert \
        -ca=ca.pem \
        -ca-key=ca-key.pem \
        -config=ca-config.json \
        -profile=kubernetes kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager
- name: 设置集群参数
kubectl config set-cluster kubernetes \
        --certificate-authority=ca.pem \
        --embed-certs=true \
        --server=https://127.0.0.1:8433 \
        --kubeconfig=kube-controller-manager.kubeconfig
- name: 设置认证参数
kubectl config set-credentials system:kube-controller-manager \
        --client-certificate=kube-controller-manager.pem \
        --client-key=kube-controller-manager-key.pem \
        --embed-certs=true \
        --kubeconfig=kube-controller-manager.kubeconfig

- name: 设置上下文参数
kubectl config set-context default \
        --cluster=kubernetes \
        --user=system:kube-controller-manager \
        --kubeconfig=kube-controller-manager.kubeconfig

- name: 选择默认上下文
kubectl config use-context default \
   --kubeconfig=kube-controller-manager.kubeconfig
```

## scedule
```
scedule.sh
- name: 准备kube-scheduler 证书签名请求
  template: src=kube-scheduler-csr.json.j2 dest={{ cluster_dir }}/ssl/kube-scheduler-csr.json

- name: 创建 kube-scheduler证书与私钥
cfssl gencert \
        -ca=ca.pem \
        -ca-key=ca-key.pem \
        -config=ca-config.json \
        -profile=kubernetes kube-scheduler-csr.json | cfssljson -bare kube-scheduler

- name: 设置集群参数
kubectl config set-cluster kubernetes \
        --certificate-authorityca.pem \
        --embed-certs=true \
        --server=https://127.0.0.1:8433 \
        --kubeconfig=kube-scheduler.kubeconfig

- name: 设置认证参数
kubectl config set-credentials system:kube-scheduler \
        --client-certificate=kube-scheduler.pem \
        --client-key=kube-scheduler-key.pem \
        --embed-certs=true \
        --kubeconfig=kube-scheduler.kubeconfig

- name: 设置上下文参数
kubectl config set-context default \
        --cluster=kubernetes \
        --user=system:kube-scheduler \
        --kubeconfig=kube-scheduler.kubeconfig

- name: 选择默认上下文
kubectl config use-context default \
   --kubeconfig=kube-scheduler.kubeconfig
```

```
systemctl daemon-reload
systemctl enanble kube-controller-manager
systemctl start kube-controller-manager
```
## kube-proxy
```
proxy.sh
```

## kubelet
```
let.sh
```