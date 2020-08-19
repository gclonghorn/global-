(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7ea5f949"],{"0767":function(e,t,i){"use strict";i.r(t);var s=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{directives:[{name:"web-title",rawName:"v-web-title",value:{title:e.webTitle},expression:"{title:webTitle}"}],staticClass:"myTeams"},[i("el-col",{attrs:{span:4}},[i("work-space")],1),i("el-col",{attrs:{span:20}}),i("el-container",[i("el-main",[i("h3",[e._v("我的团队")]),i("el-row",{attrs:{gutter:35}},e._l(e.teams,(function(t,s){return i("el-col",{key:s,staticStyle:{"margin-bottom":"20px"},attrs:{span:4}},[i("div",{staticStyle:{"text-align":"center",height:"100px"}},[i("el-card",{staticClass:"teamCard",attrs:{shadow:"hover"},nativeOn:{mouseenter:function(t){e.isHover=!0},mouseleave:function(t){e.isHover=!1}}},[e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"5px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"查看团队信息"}},[i("i",{staticClass:"el-icon-s-tools",on:{click:function(i){return e.handleClick(t.id)}}})])],1):e._e(),e.isHover?i("div",{staticStyle:{right:"5px","line-height":"5px",position:"absolute",top:"25px","font-size":"x-small"}},[i("el-tooltip",{attrs:{effect:"dark",placement:"bottom","hide-after":800,enterable:!1,content:"添加队员"}},[i("i",{staticClass:"el-icon-s-custom",on:{click:function(i){return e.addPeople(t.id)}}})])],1):e._e(),i("div",{staticStyle:{"font-size":"40px"}},[i("i",{staticClass:"el-icon-pie-chart",on:{click:function(i){return e.toOneTeam(t.id)}}})]),i("div",{staticStyle:{cursor:"pointer"},on:{click:function(i){return e.toOneTeam(t.id)}}},[e._v(e._s(t.name))])])],1)])})),1)],1),i("el-aside",{staticStyle:{"text-align":"center",padding:"50px","line-height":"80px"}},[i("div",[i("el-button",{attrs:{plain:"",type:"primary"},on:{click:e.newTeam}},[e._v("创建团队")])],1)])],1),i("el-dialog",{attrs:{title:"团队详细信息",visible:e.infoDialog,width:"30%",center:""},on:{"update:visible":function(t){e.infoDialog=t}}},[i("div",[i("div",[i("span",{staticStyle:{width:"120px",display:"inline-block"}},[e._v("团队名：")]),e._v(e._s(e.Info.name))]),i("div",[i("span",{staticStyle:{width:"120px",display:"inline-block"}},[e._v("创建者：")]),i("span",{staticStyle:{cursor:"pointer"},on:{click:function(t){return e.toPerson(e.Info.builderId)}}},[e._v(e._s(e.Info.builder))])]),i("div",[i("span",{staticStyle:{width:"40px"}},[e._v("创建日期：")]),e._v(e._s(e.Info.create_time))]),i("el-divider"),i("div",[e._v("所有成员： "),e._l(e.Info.coworkers,(function(t,s){return i("div",{key:s,staticClass:"coworkers"},[i("el-avatar",{staticStyle:{cursor:"pointer","vertical-align":"middle"},attrs:{src:t.userImg,size:"small"}}),i("span",{staticStyle:{height:"28px","padding-right":"15px","margin-left":"10px"}},[e._v(e._s(t.userName))]),t.isBuilder?i("i",{staticClass:"el-icon-user"}):e._e(),e.isCo?i("el-link",{staticStyle:{position:"absolute",right:"15px",top:"10px"},attrs:{type:"danger"},on:{click:function(i){return e.checkMove(t)}}},[t.isBuilder||e.userId!==e.Info.builderId+""?!t.isBuilder&&e.isCo?i("span",[e._v("退出")]):e._e():i("span",[e._v("移除")])]):e._e()],1)}))],2),e.userId===e.Info.builderId+""?i("el-divider"):e._e(),e.userId===e.Info.builderId+""?i("el-link",{staticStyle:{float:"right","font-size":"16px"},attrs:{plain:"",type:"danger"},on:{click:function(t){return e.Delete(e.Info.id)}}},[i("span",[e._v("删除")])]):e._e()],1)]),i("folder-dialog",{attrs:{dialog:e.folderDialog,"doc-id":e.dialogTeam,type:e.type,name:e.NAME},on:{changeVisible:e.changeVisible}})],1)},n=[],a=(i("4160"),i("b0c0"),i("159b"),i("4ec3")),o=i("56d7"),r={name:"myTeam",data:function(){return{isCo:!1,webTitle:"团队空间",userId:localStorage.getItem("userId"),teams:[],folderDialog:!1,type:"",dialogTeam:"",Info:{id:1,builder:"Kelly",coworkers:[{userId:1,userName:"Kelly",isBuilder:!0,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"},{userId:2,userName:"Kelly2",isBuilder:!1,isCollected:!0,userImg:"https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"}]},infoDialog:!1,isHover:!1,NAME:""}},mounted:function(){this.init()},methods:{init:function(){var e=this;Object(a["u"])().then((function(t){200===t.status&&(e.teams=[],t.data.forEach((function(t){e.teams.push({id:t.id,name:t.name,create_time:Object(o["GetTime"])(t.create_time),builder:t.create_user.username,builderId:t.create_user.id})})))}))},toOneTeam:function(e){this.$router.push({name:"team",params:{teamId:e}})},changeVisible:function(e){this.folderDialog=e,this.init()},newTeam:function(){this.type="newteam",this.folderDialog=!0},addPeople:function(e){var t=this;this.type="teamwork",this.dialogTeam=e,this.teams.forEach((function(i){i.id+""!==e+""||(t.NAME=i.name)})),console.log(this.NAME),this.folderDialog=!0},handleClick:function(e){var t=this;this.teams.forEach((function(i){i.id===e&&(t.Info=i)})),Object(a["o"])(this.Info.id).then((function(e){t.Info.coworkers=[],console.log(e.data),t.isCo=!1,e.data.forEach((function(e,i){e.id+""===t.userId&&(t.isCo=!0),console.log(t.isCo),0===i&&(t.Info.builder=e.username,t.Info.builderId=e.id),t.Info.coworkers.push({userId:e.id,userName:e.username,userImg:e.head,isBuilder:1===e.role}),console.log(e.id,t.Info.coworkers)})),t.infoDialog=!0})).catch((function(e){t.$message({message:e.response.data,typd:"error"})}))},Delete:function(e){var t=this;if(this.userId===this.Info.builderId){var i="确定要退出团队吗？";this.$confirm(i).then((function(){Object(a["I"])(e,localStorage.getItem("userId")).then((function(e){200===e.status?t.$message({message:"退出团队成功",type:"warning"}):204==e.status&&t.$message({message:"发生其他错误，退出团队失败",type:"error"})})).catch((function(e){e.response&&401===e.response.status&&t.$message({message:"您没有删除权限或此人不在协作者中",type:"error"})}))}))}else{var s="确定要删除团队吗？";this.$confirm(s).then((function(){Object(a["h"])(e).then((function(e){204===e.status&&(t.$message({message:"删除团队成功",type:"info"}),t.init())})).catch((function(e){return t.$message({message:e.response.data,type:"error"})})),t.infoDialog=!1}))}},checkMove:function(e){var t=this,i="确定要移除ta吗？";this.$confirm(i).then((function(){Object(a["I"])(t.Info.id,e.userId).then((function(e){200===e.status?(t.Info.coworkers=[],e.data.forEach((function(e,i){0===i&&(t.Info.builder=e.username,t.Info.builderId=e.id),t.Info.coworkers.push({userId:e.id,userName:e.username,userImg:e.head,isBuilder:1===e.role})})),t.init(),t.Dialog=!1,t.$message({message:"移除成功",type:"info"})):t.$message({message:"发生其他错误",type:"error"})})).catch((function(e){401===e.response.status&&t.$message({message:"您没有删除权限或此人不在团队中",type:"error"})})),t.infoDialog=!1}))}}},l=r,c=(i("a3f2"),i("2877")),d=Object(c["a"])(l,s,n,!1,null,"746b4a61",null);t["default"]=d.exports},"902a":function(e,t,i){},a3f2:function(e,t,i){"use strict";var s=i("902a"),n=i.n(s);n.a}}]);
//# sourceMappingURL=chunk-7ea5f949.5272c5cb.js.map