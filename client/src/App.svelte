<script>
  import Form from "./Form.svelte";
  import OutputDisplay from "./Output.svelte";
</script>

<main>
  <header>
    <h1>PassGen</h1>
  </header>

  <Form />

  <h4>Your password is:</h4>
  <OutputDisplay />

  <footer>
    <h4>&copy; 2022 Holger Mueller</h4>
  </footer>
</main>

<style>
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
    text-align: center;
  }

  h4 {
    width: 85%;
    margin: 8px auto;
  }

  footer {
    background-color: #ff3e00;
    color: white;
    bottom: 0;
    left: 0;
    position: fixed;
    width: 100%;
    text-align: center;
  }
</style>
