<template>
  <div id="app">
    <el-container>
      <el-header>
        <div class="nav">
          <router-link to="/">天气情况</router-link>
          <router-link to="/txt-getter">TXT生成器</router-link>
          <router-link to="/display/d1">气象展示系统</router-link>
        </div>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.nav{
  line-height: 60px;
  float: right;
  margin-right: 20%;
}
.nav a{
  margin-right: 30px;
  color: black;
  text-decoration: none;
  font-size: 1.2em;
}
.el-main{
  margin-top: 5%;
}
</style>
