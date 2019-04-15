<template>
  <div id="display-2">
    <el-row>
      <el-col :span="12">
        <div>
          <p>2-a</p>
          <img class="img" src="@/assets/2-a.png" alt="2-a" />
        </div>
      </el-col>
      <el-col :span="12">
        <div>
          <p>2-b</p>
          <img class="img" src="@/assets/2-b.png" alt="2-b" />
        </div>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-table
        class="weatherTable"
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="type"
          label="数据类型\数据来源"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="徐汇网站"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="1865气象站"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="1866气象站">
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
import ShowInfo from '@/components/ShowInfo.vue'


export default {
  name: 'display-2',
  components: {
    ShowInfo
  },
  data() {
    return {
      tableData: [{
        type: 'PM2.5',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        type: '风向',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        type: '风速',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        type: '空气湿度',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }, {
        type: '环境湿度',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
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
