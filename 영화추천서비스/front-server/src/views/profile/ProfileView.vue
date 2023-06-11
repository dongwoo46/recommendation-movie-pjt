<template>
  <div >
    <div class="user-profile bg-black" v-if="!isEdit">
      <img :src="selectedImage" alt="Profile Image" class="profile-image">
      <div class="profile-info">
        <h2 class="username" style="color: gold;">{{ user.name }}</h2>
        <button @click="follow" v-if="followers.includes($route.params.username)">팔로잉</button>
        <button @click="follow" v-else>팔로우</button>
        <br><br>
        <div >
          <router-link id="follow" :to="{ name: 'FollowerView' , params: { username: this.$route.params.username }}" style="text-decoration: none;" class="p-3">팔로워 : {{followers.length}}</router-link>
          <router-link id="follow" :to="{ name: 'FollowingView', params: { username: this.$route.params.username }}" style="text-decoration: none;" class="p-3">팔로잉 : {{followings.length}}</router-link>
        </div>
        <br>
        
        <p v-if="user.introduction" id="self-introduction">소개: {{user.introduction}}</p>
        <p v-else style="color:gray;">소개를 입력해주세요.</p>
        <br>
        <div id="profiletext">
          <p>성별 : {{user.sex}}</p>
          <p>키 : {{user.height}}</p>
          <p>외모 : {{user.face}}</p>
          <p>체형 : {{user.body_shape}}</p>
          <p>이상형 : {{user.ideal_type}}</p>
          <p>사는 곳 : {{user.living}}</p>
        </div>
        <div class="d-flex">
          <img :src="selectedImageSub1" alt="Profile Image" class="profile-image-sub">
          <img :src="selectedImageSub2" alt="Profile Image" class="profile-image-sub">
          <img :src="selectedImageSub3" alt="Profile Image" class="profile-image-sub">
        </div>
        <br><br>
        <button @click="editProfile" v-if="this.$route.params.username === this.$store.state.userName">수정하기</button>
      </div>
    </div>
    
    <div class="user-profile-edit bg-black" v-else>
      <br>
      <div>
        <h2 id="profileedittitle">프로필 편집</h2>
        <input type="submit" @click="back" value="뒤로가기">

      </div>
      <br>
      <form @submit.prevent="saveUserData" id="profileform">
        <!-- 성별선택 -->
        <div class="form-group">
          <div class="border border-white p-3">
            <div class="form-check" @click="check1">
              <!-- <img src="/assets/man.png" alt="man" style="max-height: auto; width: auto;" > -->
              <label style="color:blue;" class="form-check-label" for="flexRadioDefault1"> 
                남자
              </label>
              <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" >
            </div>
            <hr style="color: white;">
            <div class="form-check" @click="check2">
              <label style="color:red;" class="form-check-label" for="flexRadioDefault2">
                여자
              </label>
              <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" >
            </div>
          </div>
        </div>
        <br>
        <!-- 소개글작성 -->
        <div class="border border-white p-3">
          <div class="form-group">
            <label for="introduction">소개</label>
            <textarea id="introduction" v-model="formData.introduction" class="form-control input-narrow"></textarea>
          </div>
          <br>
        <!-- 키 작성 -->
          <div class="form-group">
            <label for="introduction">키</label>
            <textarea id="introduction" v-model="formData.person.height" class="form-control input-narrow"></textarea>
          </div>
          <br>
          <div class="form-group">
            <label for="introduction">외모</label>
            <textarea id="introduction" v-model="formData.person.face" class="form-control input-narrow"></textarea>
          </div>
          <br>
          <div class="form-group">
            <label for="introduction">체형</label>
            <textarea id="introduction" v-model="formData.person.body_shape" class="form-control input-narrow"></textarea>
          </div>
          <br>
          <div class="form-group">
            <label for="introduction">이상형</label>
            <textarea id="introduction" v-model="formData.person.ideal_type" class="form-control input-narrow"></textarea>
          </div>
          <br>
          <div class="form-group">
            <label for="introduction">사는곳</label>
            <textarea id="introduction" v-model="formData.person.living" class="form-control input-narrow"></textarea>
          </div>
          <br>
          <div class="profile-image">
            <!-- <img :src="this.user.profileImage1" alt="Profile Image" > -->
            <br>
            <input type="file" accept="image/*" @change="handleFileChange" />
            <input type="file" accept="image/*" @change="handleFileChangeSub1" />
            <input type="file" accept="image/*" @change="handleFileChangeSub2" />
            <input type="file" accept="image/*" @change="handleFileChangeSub3" />
          </div>
        </div>
        
        <br><br><br>
        <button class="btn btn-primary">저장</button>
      </form>
      
    </div>
    <!-- 댓글 구현하기 -->
    <!-- 프로필주인 - 로그인되어있는사람 -->
    
    <div v-for="(profileComment, index) in profileComments" :key="index" >
      <div class="profilecomment border border-warning p-2">
        {{profileComment.content}}
        <!-- <router-link
        :to="{name: 'ProfileView', params: { username: profileComment.username }}" style="text-decoration: none">
        {{profileComment.user.username}}
      </router-link> -->
        <p >{{profileComment.updated_at.slice(0,10)}} {{profileComment.updated_at.slice(11,16)}}</p>
      </div>   
    </div>
    
    <form v-if="this.$route.params.username !== this.$store.state.userName" @submit.prevent="createComment" @keyup.enter="createComment">
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea
          v-model="newComment.content"
          class="form-control"
          id="content"
          rows="3"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">댓글 작성</button>
    </form>
  </div>  
</template>

<script>

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      isFollowed: false,
      newComment: {'content':null,},
      profileComments: [],
      selectedImage: null,
      selectedImageSub1: null,
      selectedImageSub2: null,
      selectedImageSub3: null,
      isCheck1: false,
      isCheck2: false,
      followers: [],
      followings: [],
      userName: this.$route.params.username,
      user: {
        name: null,
        profileImage1: null, // 프로필이미지 띄울꺼
        profileImage2: null,
        profileImage3: null,
        profileImage4: null,
        sex: null,
        introduction: null,
        height: null,
        body_shape: null,
        face: null,
        ideal_type: null,
        living: null,
        likeMovie: [],
      },
      isEdit: false,
      formData: {
        introduction: '',
        person: {
          'height': null,
          'body_shape': null,
          'face': null,
          'ideal_type': null,
          'living': null,
        }
      },
    };
  },

  created() {
    window.scrollTo({
        top: 0,
        // behavior: 'smooth',
      });


      this.getComment()
      this.fetchFollowers()
      this.fetchFollowings()
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/${this.userName}`,
        })
        .then(res => {
          this.user.name = res.data.username
          this.user.profileImage = res.data.profile_img
          this.user.introduction = res.data.introduction
          this.user.height = res.data.height
          this.user.body_shape = res.data.body_shape
          this.user.face = res.data.face
          this.user.ideal_type = res.data.ideal_type
          this.user.living = res.data.living
          this.user.sex = res.data.sex
        })
        .catch(err => {
          console.log(err)
        })
  },
  methods: {
    back() {
      this.isEdit = !this.isEdit
    },
    getComment(){
      axios({
            method:'get',
            url:`${API_URL}/accounts/profile/${this.$route.params.username }/comments/`,
            headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
          })
          .then(res => {
            this.profileComments = res.data
          })
    },
    createComment() {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/profile/${this.$route.params.username}/comments/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
          },
          data: this.newComment
        })
        .then(res => {
          this.profileComments.push(res.data)
          this.newComment.content = '';
        })
        .catch(err=>{
          console.log(err)
        })
      },
    check1() {
      if (this.isCheck2){
        this.isCheck1 = true
        this.isCheck2 = false
      }
      else{
        this.isCheck1 = true
      }
    },
    check2() {
      if (this.isCheck1){
        this.isCheck1 = false
        this.isCheck2 = true
      }
      else{
        this.isCheck2 = true
      }
    },

    editProfile() {
      this.isEdit = !this.isEdit
    },
    handleFileChange(event) {
      this.selectedImage = URL.createObjectURL(event.target.files[0])
    },
    handleFileChangeSub1(event) {
      this.selectedImageSub1 = URL.createObjectURL(event.target.files[0])
    },
    handleFileChangeSub2(event) {
      this.selectedImageSub2 = URL.createObjectURL(event.target.files[0])
    },
    handleFileChangeSub3(event) {
      this.selectedImageSub3 = URL.createObjectURL(event.target.files[0])
    },
    saveUserData() {
      window.scrollTo({
        top: 0,
        // behavior: 'smooth',
      });

      // 이미지 파일 로컬 스토리지에 저장
      localStorage.setItem(`${this.$route.params.username}`, this.selectedImage)
      localStorage.setItem(`${this.$route.params.username}Sub1`, this.selectedImageSub1)
      localStorage.setItem(`${this.$route.params.username}Sub2`, this.selectedImageSub2)
      localStorage.setItem(`${this.$route.params.username}Sub3`, this.selectedImageSub3)


      const introduction = this.formData.introduction
      const height = this.formData.person.height
      const body_shape = this.formData.person.body_shape
      const face = this.formData.person.face
      const ideal_type = this.formData.person.ideal_type
      const living = this.formData.person.living
      let sex

      if (this.isCheck1){
        sex = "남자"
        this.user.sex = sex
        
      }
      else if (this.isCheck2) {
        sex = "여자"
        this.user.sex = sex
      }

      
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/profile/${this.$store.state.userName}/`,
        data : {
          // formData,
          introduction,
          height,
          body_shape,
          face,
          ideal_type,
          living,
          sex,
        },
      })
      .then(res => {
        this.user.name = res.data.username
        this.user.introduction = res.data.introduction
        this.user.height = res.data.height
        this.user.body_shape = res.data.body_shape
        this.user.face = res.data.face
        this.user.ideal_type = res.data.ideal_type
        this.user.living = res.data.living
      })
      .catch(err => {
        console.log(err)
      })
      this.isEdit = !this.isEdit
    },
    fetchFollowers() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.username}/followers_list/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
          }
      })
      .then(res => {
        for (const user of res.data){
          this.followers.push(user.username)
        }
        this.$store.state.currentUserFollowers = this.followers
      })
      .catch(error => {
        console.log(error);
      })
    },
    fetchFollowings() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.username}/followings_list/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
          }
      })
      .then(res => {
        for (const user of res.data){
          this.followings.push(user.username)
        }
        this.$store.state.currentUserFollowings = this.followings
      })
      .catch(error => {
        console.log(error);
      })
    },
    follow() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.username}/follow/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
          }
      })
      .then(res => {
        console.log(res.data.followings)
        this.fetchFollowers()
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    const savedImage = localStorage.getItem(`${this.$route.params.username}`)
    const savedImageSub1 = localStorage.getItem(`${this.$route.params.username}Sub1`)
    const savedImageSub2 = localStorage.getItem(`${this.$route.params.username}Sub2`)
    const savedImageSub3 = localStorage.getItem(`${this.$route.params.username}Sub3`)
    if (savedImage) {
      this.selectedImage = savedImage;
    }
    if (savedImageSub1) {
      this.selectedImageSub1 = savedImageSub1;
    }
    if (savedImageSub2) {
      this.selectedImageSub2 = savedImageSub2;
    }
    if (savedImageSub3) {
      this.selectedImageSub3 = savedImageSub3;
    }
  },

};
</script>

<style>
.user-profile {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background-color: #f5f5f5;
  font-family: Arial, sans-serif;
}

.profile-image img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.profile-image-sub {
  width: 150px;
  height: 150px;
  /* border-radius: 50%; */
  object-fit: cover;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.profile-info {
  margin-left: 40px;
  font-family: 'Gugi', cursive;
}

.username {
  font-size: 50px;
  font-weight: bold;
  margin-bottom: 10px;
}

.email {
  font-size: 16px;
  margin-bottom: 10px;
  color: #666666;
}

.bio {
  margin-bottom: 20px;
  color: #888888;
}

.interests {
  margin-top: 10px;
}

.interests-heading {
  font-size: 18px;
  font-weight: bold;
  color: #333333;
  margin-bottom: 10px;
}

.interests-list {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
}

.interest-item {
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 8px 12px;
  background-color: #f2f2f2;
  color: #333333;
  border-radius: 4px;
  font-size: 14px;
}

form {
  margin-left: 500px;
  margin-right: 500px;
}

label {
  color: white
}

#follow {
  color: rgb(130, 130, 240);
}

#profiletext {
  font-size: x-large;
}

#self-introduction {
  padding: 10px;
  border: 2px  solid gold;
  border-radius: 5%;
}
#profileedittitle {
  color: gold;
  font-family: 'Gugi', cursive;
}

.user-profile-edit{
  font-size: x-large;
  font-family: 'Black Han Sans', sans-serif;
}

.profilecomment{
  font-size: 20px;
  color: white;
}
.profile-image {
  float: left;
  margin-right: 20px;
  width: 300px; /* 이미지 크기 조정에 맞게 변경 가능 */
  height: 300px;
  object-fit: cover;
  border-radius: 50%;
}

</style>
