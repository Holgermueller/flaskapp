<script>
  function copyPassword() {
    const copyText = document.getElementById("passwordToCopy").value;
    console.log(copyText);
    navigator.clipboard.writeText(copyText);
  }
</script>

<div class="output-display">
  <input class="output" id="passwordToCopy" type="text" value="Output" />
  <button id="copy" on:click={copyPassword}>
    <i class="fa-solid fa-clipboard" />
  </button>
</div>

<style>
  .output-display {
    width: 85%;
    margin: 8px auto;
    border: 1px solid gray;
    border-radius: 15px;
  }

  .output {
    margin: auto;
    width: 85%;
    letter-spacing: 6px;
    text-align: center;
    border: 0;
    background: transparent;
  }
  button {
    border: 0;
    background-color: inherit;
    float: right;
    margin-right: 8px;
  }
</style>
