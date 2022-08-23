<script>
  export let name;
</script>

<main>
  <header>
    <h1>PassGen</h1>
  </header>

  <div class="form">Input goes here</div>

  <div class="output">output goes here</div>

  <footer>
    <h4>&copy; 2022 Holger Mueller</h4>
  </footer>
</main>

<style>
  main {
    text-align: center;
    margin: 0 auto;
  }

  header {
    top: 0;
    right: 0;
    width: 100%;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 50px;
    font-weight: 100;
  }

  footer {
    background-color: #ff3e00;
    color: white;
    bottom: 0;
    left: 0;
    position: fixed;
    width: 100%;
  }
</style>
