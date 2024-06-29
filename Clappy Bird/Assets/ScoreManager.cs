using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class ScoreManager : MonoBehaviour
{
    public BirdController birdController;
    public ObstacleSpawner obstacleSpawner;
    public TextMeshProUGUI scoreText;
    public float startDelay = 2f;

    private int score;
    private float timeSinceLastScore;
    private float scoreInterval;
    private bool startDelayElapsed;

    void Start()
    {
        score = 0;
        UpdateScoreText();
        timeSinceLastScore = 0f;
        scoreInterval = obstacleSpawner.spawnInterval;
        startDelayElapsed = false;
        StartCoroutine(StartDelay());
    }

    void Update()
    {
        if (birdController.HasStarted() && startDelayElapsed)
        {
            timeSinceLastScore += Time.deltaTime;

            if (timeSinceLastScore >= scoreInterval)
            {
                IncrementScore();
                timeSinceLastScore = 0;
            }
        }
    }

    void IncrementScore()
    {
        score++;
        UpdateScoreText();
    }

    void UpdateScoreText()
    {
        scoreText.text = score.ToString();
    }

    IEnumerator StartDelay()
    {
        yield return new WaitForSeconds(startDelay);
        startDelayElapsed = true;
    }
}
