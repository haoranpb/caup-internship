<template>
  <div id="display-2">
    <el-row>
      <el-col :span="12">
        <div style="position: relative;left: 30%;">
          <p>2-a</p>
          <img class="img" src="@/assets/2-a.png" alt="2-a" />
        </div>
      </el-col>
      <el-col :span="12">
        <div style="position: relative;right: 30%;">
          <p>2-b</p>
          <img class="img" src="@/assets/2-b.png" alt="2-b" />
        </div>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-table class="weatherTable" :data="tableData" style="width: 100%">
        <el-table-column prop="type" label="数据类型\数据来源" width="180"></el-table-column>
        <el-table-column prop="datax" label="徐汇网站" width="180"></el-table-column>
        <el-table-column prop="data5" label="1865气象站" width="180"></el-table-column>
        <el-table-column prop="data6" label="1866气象站"></el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'display-2',
  data() {
    return {
      tableData: [{
        type: 'PM2.5',
        datax: 'datax',
        data5: 'data5',
        data6: 'data6'
      }]
    }
  },
  mounted: function(){
    let obj = this;

    axios.get('http://ludanxer.top:10000/crawl-data')
    .then(function(response) {
      let data = response.data;
      let labels = ['PM2.5(ug/m3)', '环境湿度(%)', '空气温度(℃)', '风向(度)', '风速(m/s)'];
      obj.tableData = [];
      for(let label of labels){
        let tmp = {};
        tmp['type'] = label;
        tmp['data5'] = data['1865'][label];
        tmp['data6'] = data['1866'][label];
        obj.tableData.push(tmp);
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });

    axios.get('http://ludanxer.top/projects/caup/xuhui.txt')
    .then(function(response) {
      let data = response.data.split('\n');
      for(let i in data){
        let tmp= data[i].split(' ');
        obj.tableData[i]['datax'] = tmp[1];
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });    
  }
}
</script>

<style>
.weatherTable{
  margin-left: 20%;
  margin-right: 20%;
  widows: 60%;
}
</style>
