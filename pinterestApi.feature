Feature: Pinterest API autamted test


  Scenario: Check if user authenticated
    Given we get authenticated user info
    Then responce should contain user id


    Scenario: User can subscribe to a board and unsubscribe
      Given we are authenticated
      And we are not following board nasa/mars
      Then we follow nasa/mars
      And we should see nasa/mars in our boards list
      Then we unfollow nasa/mars
      And we should not see nasa/mars in our boards list