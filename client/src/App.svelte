<script>
  function copyPassword() {
    const copyText = document.getElementById("passwordToCopy").value;
    console.log(copyText);
    navigator.clipboard.writeText(copyText);
  }
</script>

<main>
  <header>
    <h1>PassGen</h1>
  </header>

  <form action="" class="form">
    <label for="pass_length">Password Length</label>
    <input type="number" name="pass_length" id="pass_length" value="8" />
    <br />
    <small>Your password must be at least 8 characters long</small>

    <div class="form-group">
      <label class="check-label" for="">Has Numbers?</label>
      <select name="has_numbers" id="hasNumbers">
        <option value="yes">Yes</option>
        <option value="no">No</option>
      </select>
    </div>

    <div class="form-group">
      <label class="check-label" for="">Has Special Characters?</label>
      <select name="has_numbers" id="hasNumbers">
        <option value="yes">Yes</option>
        <option value="no">No</option>
      </select>
    </div>

    <input type="submit" value="Submit" />
  </form>

  <div class="output-display">
    <input class="output" id="passwordToCopy" type="text" value="Output" />
    <button id="copy" on:click={copyPassword}>
      <i class="fa-solid fa-clipboard" />
    </button>
  </div>

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

  form,
  .output-display {
    width: 85%;
    margin: auto;
  }

  input {
    width: 95%;
    margin: 8px auto;
    border-radius: 5px;
  }
  input[type="number"] {
    text-align: right;
    margin-right: 4px;
  }

  small {
    text-align: left;
    padding: 8px 0;
    width: 100%;
  }

  .form-group {
    padding: 8px;
  }
  select {
    border-radius: 5px;
    width: 15%;
    letter-spacing: 3px;
  }

  .check-label {
    text-align: left;
    padding: 4px;
  }

  input[type="submit"] {
    color: white;
    background-color: slategray;
  }

  .output-display {
    margin: 8px auto;
    border: 1px solid gray;
    border-radius: 15px;
  }

  .output {
    width: 90%;
    letter-spacing: 6px;
    text-align: center;
    border: 0;
  }
  button {
    border: 0;
    background-color: inherit;
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
