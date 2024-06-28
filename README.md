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

runc
```
https://github.com/opencontainers/runc/
```

## api server
```
api.sh
```

## manager
```
manager.sh
```

## scedule
```
scedule.sh
```

## kube-proxy
```
proxy.sh
```

## kubelet
```
let.sh
```