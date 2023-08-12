# bilibili_fans_record
一个可以同时记录多个用户粉丝数变化为特定格式的txt文档的python程序。
<h3>具体用法</h3>
安装好依赖库并更改好uid等相应参数后直接运行即可。
<h3>相关参数</h3>
<h5>基础</h5>
jump：每轮爬取的间隔，单位为秒。不建议太低以免被ban。请注意每个用户抓取时间间隔，实际jump = 目标jump - 抓取的用户数量 * 每个uid抓取间隔(即下面提到的wait) + 1。<br>
uids：目标用户的id号，格式参照示例即可。<br>
<h5>进阶</h5>
wait：一轮爬取中，每个目标数据的爬取间隔。若目标较少，且jump较大，则可以wait值可以较小。若目标较多或jump较小时，则wait不宜过小，以防止IP被ban。<br>
可以将“文档”二字更改为你想要的文件夹名，该文件夹位于与主程序同级的目录上。<br>
本版本默认以wikitext的格式进行保存，在wikitext模式下将直接显示为表格。您可以通过修改file_handle.write后及str2 = 后内容改变记录格式，但我们十分不建议您这样做，因为这可能导致记录排版混乱。<br>
<h5>定时器版本操作说明</h5>
本版本可在每日特定时间开始新一轮记录，而取消使用倒计时。<br>
本版本中，jump为无效参数，可不予以理会。<br>
更改time_interval的参数即可实现记录时间的更改。<b>注意：更改的参数时，应该严格保证time_interval的区间为1分钟。</b>(即time_interval = Interval("HH:MM:SS", "HH:MM+1:SS"))<br>
您可以增删time_interval以增删记录时间点；增删time_interval时您应当同步增删相应的诸如 now_time in time_interval 的字段。<br>
<h5>json版本的操作说明</h5>
json版参数基本上与定时器版本一致，只是改用了json格式储存，机器可读性更好<br>
json版本推荐使用<code>.config</code>储存要观测的uid，其中用形如<code>[2,114514,1919810,...]</code>的格式储存即可<br>
具体实例可参考 我们制作的粉丝观测小站: http://www.pro-ivan.com/bilibili/
<hr><br>
其他内容不建议更改。
