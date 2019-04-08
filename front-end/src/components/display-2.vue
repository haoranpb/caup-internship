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
      <el-col :span="6">
        <show-info />
        <h1>2. App 数据</h1>
        <h1>3. 气象站数据</h1>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ShowInfo from '@/components/ShowInfo.vue'


export default {
  name: 'display-2',
  components: {
    ShowInfo
  }
}
</script>
