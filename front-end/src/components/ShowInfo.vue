<template>
  <div id="show-info">
    <div class="title">
      <p>上海市徐家汇区天气情况</p>
      <p>更新时间：{{ updatetime }}</p>
    </div>
    <dl class="text">
      <dd>{{ humidity }}</dd>
      <dd>{{ wind }}</dd>
      <dd>{{ ray }}</dd>
      <dd>{{ temperature }}</dd>
    </dl>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      humidity: '湿度：',
      wind: '风力：',
      ray: '紫外线：',
      temperature: ' 摄氏度',
      updatetime: ''
    }
  },
  mounted: function(){
    let element = this;
    let myMap = new Map();
    myMap.set(0, ' 无风 0.0-0.2');
    myMap.set(1, ' 软风 0.3-1.5');
    myMap.set(2, ' 轻风 1.6-3.3');
    myMap.set(3, ' 微风 3.4-5.4');
    myMap.set(4, ' 和风 5.5-7.9');
    myMap.set(5, ' 清风 8.0-10.7');
    myMap.set(6, ' 强风 10.8-13.8');
    myMap.set(7, ' 劲风（疾风） 13.9-17.1');

    axios.get('https://ludanxer.top/projects/caup/data.txt', {cache: false})
    .then(function(response){
      element.$message({
        message: 'success!',
        type: 'success'
      });
      let data = response.data.split('\n');
      element.humidity += data[0];
      element.wind += (data[1] + myMap.get(Number(data[1][3])));
      element.ray += data[2];
      element.temperature = '温度：' + data[3] + element.temperature;
      element.updatetime += data[4]
    })
    .catch(function () {
      element.$message.error('糟糕，哪里出了点问题！');
    });
  }
}
</script>

<style scoped>
.text{
  margin-top: 60px;
  text-align: left;
  line-height: 40px;
  font-size: 1.1em;
  font-weight: 500;
}
.title{
  text-align: left;
}
</style>

