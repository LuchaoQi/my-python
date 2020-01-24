# my-python

### TensorFlow and PyTorch



==A collection of various deep learning architectures, models, and tips==

https://github.com/rasbt/deeplearning-models





### tips



[Sorting-Algorithm](https://github.com/hustcc/JS-Sorting-Algorithm)



some python tips 

https://github.com/chiphuyen/python-is-cool



Run python online

> [Binder](https://mybinder.org/) is a good google colab alternative

Add your `open in google colab` badge

> <a href="https://colab.research.google.com/github.com/LuchaoQi/my-python" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
>
> ```html
> <a href="https://colab.research.google.com/github.com/LuchaoQi/my-python" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
> ```







[Yellowbrick: Machine Learning Visualization that extend the scikit-learn API](https://www.scikit-yb.org/en/latest/index.html#yellowbrick-machine-learning-visualization)





lazy-import packages [pyforest](https://github.com/8080labs/pyforest#demo-in-jupyter-notebook)

>  Note that the latest pyforest requires Java





windows: double-click to open .ipynb files 

> set system open .ipynb with this file [open_ipynb.bat](https://github.com/LuchaoQi/my-python/blob/master/open_ipynb.bat) 
>
> note this will change the start-up directory
>
> [another way to change the jupyter default start-up directory](https://mp.weixin.qq.com/s?__biz=Mzg3MTAyMDMxOQ==&mid=2247483866&idx=1&sn=9f08b1a95f4b66f91d0984484ab046e0&chksm=ce85a3aaf9f22abc8c38ebbdb3ae2380b66324954605d3f02a8c63586dd69a7e90ccabeeebf0&mpshare=1&scene=1&srcid=&sharer_sharetime=1575642056921&sharer_shareid=54d7b6bf73b347d381a7bff3f78b99d1&key=618a98a1e39c24e675f4effc46236faa89626f09b54ffb1737eae897e8c66cdb7c000259f43b833fb842aad384e23e299fce59a41ba1bc2414c2d434b7121a446dc48e0004401f6cb042c7d2f05c6950&ascene=1&uin=NzA3NTE3MTMz&devicetype=Windows+10&version=62070158&lang=en&exportkey=AxawcEAZAoYfElAbo2%2FnmAQ%3D&pass_ticket=ee2Re0y5GRDC7Z5JO2IRPQMYtoeI2sD8LkuPcXANvvpCdl6NlB9x9gylFsx2yZyu) 
>
> I realized lots of people use [nbopen](https://github.com/takluyver/nbopen) though that's not I want and too complicated :P





environment management/sync [pip/conda](https://www.jianshu.com/p/b86c17057da8?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)





Jupyter: how to let one cell block output multiple commands results

> ![](https://mmbiz.qpic.cn/mmbiz_png/qsxsdMygxBwjFVibWCRP2eicDD1UXw7NeiaJq0XQhyPPU8EvFqdiahCVmHDbWSrJvPslgpgDHTFiciajUicLFj1x72QSQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
>
> ```python
> from IPython.core.interactiveshell import InteractiveShell
> InteractiveShell.ast_node_interactivity = "all"
> ```
>
> In data science projects, I usually commend this out in my snippets b/c it will output lots of miscellaneous results when doing plots



### matplotlib

[Top 50 matplotlib Visualizations – The Master Plots (with full python code)](https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/)



### Numpy

[numpy-100](https://github.com/rougier/numpy-100)



```python
np.zeros(12).reshape(3,4) = np.zeros((3,4))
# N, number of matrices
np.random.random(N,nrow,ncol)
Z = np.ones((10,10))
# Change 1 to 0
Z[1:-1,1:4] = 0
np.pad(Z, pad_width=1, mode='constant', constant_values=0)
```



https://realpython.com/how-to-use-numpy-arange/



![image.png](https://i.loli.net/2020/01/17/nINBl2itZQ36S79.png)





### Pandas

[如何使用 Pandas 读写Excel](https://mp.weixin.qq.com/s?__biz=MzUzMTEwODk0Ng==&mid=2247489316&idx=1&sn=0119d08865fa6a9d133718798fb01f3b&chksm=fa46d219cd315b0f6cf0ea1c8cf9d5fd209f5ead7a16a9fab9c495afdc24a3a3af7b8ec39424&mpshare=1&scene=1&srcid=&sharer_sharetime=1575560110538&sharer_shareid=54d7b6bf73b347d381a7bff3f78b99d1&key=618a98a1e39c24e6c8a133fea4e983e7009683d75c15dd142887606449ef1e5b83011a2458894838729940cf8c4b46fcc81cc2e8c89364c8774eb77e5771b7cfdc845cd45bbab25f61a2cc2395fe2d88&ascene=1&uin=NzA3NTE3MTMz&devicetype=Windows+10&version=62070158&lang=en&exportkey=AwHRLcm3bj16cYvSvQt%2BML0%3D&pass_ticket=ee2Re0y5GRDC7Z5JO2IRPQMYtoeI2sD8LkuPcXANvvpCdl6NlB9x9gylFsx2yZyu)

[还在抱怨pandas运行速度慢？这几个方法会颠覆你的看法](https://mp.weixin.qq.com/s?__biz=MzU4OTQ1MTA4OQ==&mid=2247484170&idx=1&sn=8f662550a6e01ab191de1c57afb4f2e5&chksm=fdcc1934cabb9022b42ddf51c2c11f8c5069c424ac7f1120550c66dae34e395991b0b3ada92e&mpshare=1&scene=1&srcid=&sharer_sharetime=1575522959679&sharer_shareid=54d7b6bf73b347d381a7bff3f78b99d1&key=aa397d0f1c3682ba85dc210d24355b5edd123bd41da566c32115a60bdca077a4b648abf84f1b9002187ad3d77d6baec5f099e26f7a440a4e6fc85831696909e1baf3274c4bed4b32c297082c805bffff&ascene=1&uin=NzA3NTE3MTMz&devicetype=Windows+10&version=62070158&lang=en&exportkey=AxRu4fmcVlvQRThRqao5gkE%3D&pass_ticket=ee2Re0y5GRDC7Z5JO2IRPQMYtoeI2sD8LkuPcXANvvpCdl6NlB9x9gylFsx2yZyu)

[惊了！大牛换了个思路，就让 Pandas 快了 1000x！](https://mp.weixin.qq.com/s?__biz=Mzg3MTAyMDMxOQ==&mid=2247484088&idx=1&sn=bf127b42706b72ec9a4f34a9ef2df912&chksm=ce85a0c8f9f229de91b2ec02ae5ac23c6699ee66ce29e89ba9ced17fb8e3e935d0f585e6db07&mpshare=1&scene=1&srcid=012560Rv2ZXMKbhhzpWQJbJq&sharer_sharetime=1579909492329&sharer_shareid=54d7b6bf73b347d381a7bff3f78b99d1&key=47c0c8dda35b3d6ee85d69b7b662ba41d469adc671ed850dd6da47b73a8902f53a6242181efcf6e0242731d540d53e1c845a273de39984b309a2b6943e95b746b08ffb9d6c0fa66e232995ddbc268323&ascene=1&uin=NzA3NTE3MTMz&devicetype=Windows+10&version=62070158&lang=en&exportkey=A8%2BE8Kqp6Tr85gxTfxo4zu0%3D&pass_ticket=lJveRg9gAUeTqWfqKJqPTsmBETtIP04Z4E2W2kBQR9BH39IEkb5%2FusO9Aiu9jq1T)

