(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0f65fcf9"],{1550:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:"我的文档"},expression:"{title:'我的文档'}"}],staticClass:"myBuild"},[a("el-col",{attrs:{span:4}},[a("work-space")],1),a("el-col",{attrs:{span:20}}),a("el-container",[a("el-main",[a("div",{staticStyle:{"margin-top":"20px"}},[a("span",{staticStyle:{width:"50%","font-size":"1.17em","font-weight":"bold"}},[t._v("我的文档")]),a("span",{staticStyle:{float:"right"}},[a("el-radio-group",{attrs:{size:"small"},on:{change:t.changeChart},model:{value:t.chart,callback:function(e){t.chart=e},expression:"chart"}},[a("el-radio-button",{attrs:{label:"列表"}}),a("el-radio-button",{attrs:{label:"图标"}})],1)],1)]),a("div",{staticStyle:{"margin-top":"30px"}},["列表"===t.chart?a("doc-list",{ref:"child",attrs:{type:"build"}}):a("doc-img",{ref:"child",attrs:{type:"build"}})],1)]),a("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toNewDoc}},[t._v("新建文档")])],1),a("div",[a("el-button",{attrs:{plain:"",type:"primary"},on:{click:t.toTemplate}},[t._v("模板库")])],1)])],1)],1)},n=[],c=a("4ec3"),s={name:"myBuild",data:function(){return{chart:""}},mounted:function(){this.init()},methods:{init:function(){localStorage.getItem("chart")?this.chart=localStorage.getItem("chart"):this.chart="图标"},toNewDoc:function(){var t=this;Object(c["c"])(0).then((function(e){201===e.status&&(t.$message({message:"新建文档成功",type:"info"}),t.$router.push({name:"editorPage"}))})).catch((function(e){401===e.response.status&&t.$message({message:"您没有权限",type:"error"})})),this.$refs.child.init()},changeChart:function(t){this.chart=t,localStorage.setItem("chart",t)},toTemplate:function(){this.$router.push({name:"templates"})}}},r=s,l=(a("5415"),a("2877")),o=Object(l["a"])(r,i,n,!1,null,"18b838f1",null);e["default"]=o.exports},"37f4":function(t,e,a){},5415:function(t,e,a){"use strict";var i=a("37f4"),n=a.n(i);n.a}}]);