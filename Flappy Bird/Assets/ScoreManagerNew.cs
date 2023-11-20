using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class ScoreManagerNew : MonoBehaviour
{
    public TextMeshProUGUI scText;
    public BirdController birdController;

    void Update()
    {
        scText.text = birdController.playerScore.ToString();
    }

    public void restart()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
