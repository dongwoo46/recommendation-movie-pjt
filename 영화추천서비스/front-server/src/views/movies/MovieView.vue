<template>
  <div class="moviegugi ">
    <h3 style="font-size:50px; color:gold;">최신 영화</h3>
    <!-- 액션 영화 목록 -->
    <h3>액션</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['action']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.Movie_pk)">
        </div>
      </div>
    </div>
    <!-- 코미디 목록 -->
    <h3>코미디</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['comedy']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 로맨스 목록 -->
    <h3>로맨스</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['romance']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 드라마 목록 -->
    <h3>드라마</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['drama']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 공포 목록 -->
    <h3>공포</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['horror']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 스릴러 & 범죄 목록 -->
    <h3>스릴러 & 범죄</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['thriller']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 판타지 목록 -->
    <h3>판타지</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['fantasy']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img  class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 애니 목록 -->
    <h3>애니</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['ani']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 다큐멘터리 & 역사 목록 -->
    <h3>다큐멘터리 & 역사</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['document']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- SF 목록 -->
    <h3>SF</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['SF']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>
    <!-- 음악 목록 -->
    <h3>음악</h3>
    <div class="carousel" id="nowMovie">
        <div class="slide-container">
          <div
            class="slide"
            v-for="(movie, index) in popularMovieList['music']"
            :key="index"
            @mousedown="startTimer(index)"
            @mouseup="stopTimer"
            @mouseleave="stopTimer"
          >
          <img class="movie-detail" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="poster" v-if="movie.poster_path" @click="movieDetail(movie.id)">
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieView',
    data() {
        return {
          popularMovieList: {
            'action' : [],
            'comedy' : [],
            'family' : [],
            'romance': [],
            'drama': [],
            'horror': [],
            'thriller': [],
            'fantasy': [],
            'ani': [],
            'document': [],
            'SF': [],
            'music': [],
            },
        }
    },
    methods: {
      startTimer() {
        this.intervalId = setInterval(() => {
          this.nextSlide();
        }, 1000); // 일정 시간 간격으로 다음 이미지로 이동 (예: 0.2초)
      },
      stopTimer() {
        clearInterval(this.intervalId);
      },
      nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.nowMovieList.length;
      },
      prevSlide() {
        this.currentIndex = (this.currentIndex - 1 + this.nowMovieList.length) % this.nowMovieList.length;
      },
      movieDetail(moviePk) {
        this.$router.push({name: 'MovieDetailView', params: { moviePk }})
      },

    },
    mounted() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/'
        })
        .then(res => {
          this.popularMovieList['action'] = res.data.action
          this.popularMovieList['comedy'] = res.data.comedy
          this.popularMovieList['family'] = res.data.family
          this.popularMovieList['romance'] = res.data.romance
          this.popularMovieList['drama'] = res.data.drama
          this.popularMovieList['horror'] = res.data.horror
          this.popularMovieList['thriller'] = res.data.thriller
          this.popularMovieList['fantasy'] = res.data.fantasy
          this.popularMovieList['ani'] = res.data.ani
          this.popularMovieList['document'] = res.data.document
          this.popularMovieList['SF'] = res.data.SF
          this.popularMovieList['music'] = res.data.music
          })
        .catch(err => {
          console.log(err)
          })
    }
}
</script>

<style>
  .carousel {
    display: flex;
    overflow-x: scroll;
    margin-top: 30px;
  }


.movie-detail{
  transition: all 0.2s linear;
  overflow: hidden;
}

.movie-detail:hover {
  transform: scale(1.3);
}


  .slide-container {
    display: flex;
  }

  .slide {
    flex: 0 0 auto;
    margin-right: 20px;
  }

  img {
    width: 100px;
    height: 150px;
  }
  h3 {
    padding-top: 30px;
    color: white
  }

  #nowMovie {
    cursor: pointer;
  }

  .moviegugi {
    font-family: 'Gugi', cursive;
    font-size: 50px;
  }
</style>