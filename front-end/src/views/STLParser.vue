<template>
  <div id="stl">
    <el-upload
      drag
      action="http://ludanxer.top:10000/upload"
      :on-success="download"
      multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将STL文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">文件上传完成后会自动下载处理后的文件</div>
    </el-upload>
    <el-table class="dataTable"
      :data="tableData">
      <el-table-column
        prop="c"
        label="坐标"
        width="180">
      </el-table-column>
      <el-table-column
        prop="min"
        label="最小值"
        width="180">
      </el-table-column>
      <el-table-column
        prop="max"
        label="最大值">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      tableData: [{
        c: 'X',
        min: '9999',
        max: '0'
      }, {
        c: 'Y',
        min: '9999',
        max: '0'
      }, {
        c: 'Z',
        min: '9999',
        max: '0'
      }]
    }
  },
  methods: {
    download: function(response){
      let atag = document.createElement("a");
      let stl_file = new Blob([response], {type: 'text/plain'});
      atag.href = URL.createObjectURL(stl_file);
      atag.download = 'parsed.stl';
      atag.click();

      let obj = this;

      axios.get('http://ludanxer.top:10000/min-max')
      .then(function(response) {
        obj.tableData[0].min = response.data['x-min'];
        obj.tableData[0].max = response.data['x-max'];
        obj.tableData[1].min = response.data['y-min'];
        obj.tableData[1].max = response.data['y-max'];
        obj.tableData[2].min = response.data['z-min'];
        obj.tableData[2].max = response.data['z-max'];
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}
</script>

<style scoped>
.dataTable{
  margin-left: 30%;
  margin-right: 30%;
  width: 40%;
  margin-top: 5%;
}
</style>

