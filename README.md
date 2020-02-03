# my-python



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



